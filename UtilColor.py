import scipy
import scipy.cluster

from McxUtil.UtilCanvas import UtilCanvas


class UtilColor:
    #
    # 12/2017
    #
    @staticmethod
    def getDominantColors(npRGB, numColors):
        # print(npRGB.shape)
        height = npRGB.shape[0]
        width = npRGB.shape[1]

        # FIXME: extracting colors should ne in a utility function

        npOrig = npRGB  # image in original size
        if width * height > 150 * 150:
            npRGB = UtilCanvas.resize2017(npRGB, '150x150')  # to reduce time

        shape = npRGB.shape
        npRGB = npRGB.reshape(scipy.product(shape[:2]), shape[2])

        shapeOrig = npOrig.shape
        npOrig = npOrig.reshape(scipy.product(shapeOrig[:2]), shapeOrig[2])

        #print('finding clusters')
        colors, distances = scipy.cluster.vq.kmeans(npRGB, numColors)
        #print('cluster centres:\n', colors, distances)


        # ---- sort colors by count
        # vecs, distances = scipy.cluster.vq.vq(npOrig, colors)  # assign codes
        # counts = []
        # for i, color in enumerate(colors):
        #     count = len(scipy.where(vecs == i)[0])
        #     counts.append(count)
        # print(counts)
        # counts, colors = zip( *sorted( zip(counts, colors), reverse=True ) )
        # print(counts)

        return colors


    #
    # 01/2018
    #
    @staticmethod
    def recolorImage(npOrig, colors):
        shapeOrig = npOrig.shape
        npOrig = npOrig.reshape(scipy.product(shapeOrig[:2]), shapeOrig[2])
        vecs, distances = scipy.cluster.vq.vq(npOrig, colors)  # assign codes
        # print("vecs", vecs.shape, "dist", distances.shape)

        # counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences
        # print bins
        # index_max = scipy.argmax(counts)                    # find most frequent
        # peak = codes[index_max]
        # colour = ''.join(chr(c) for c in peak).encode('hex')
        # print 'most frequent is %s (#%s)' % (peak, colour)

        # generate image using only the N most common colours
        c = npOrig  # .copy()
        for i, color in enumerate(colors):
            c[scipy.r_[scipy.where(vecs == i)], :] = color
        # scipy.misc.imsave('clusters.png', c.reshape(*shape))
        # print 'saved clustered image'
        res = c.reshape(*shapeOrig)

        return res
