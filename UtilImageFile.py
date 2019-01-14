import imageio
import numpy as np

from McxUtil.UtilCanvas import UtilCanvas
from McxUtil.UtilMap import UtilMap


class UtilImageFile:

    @classmethod
    def saveNumpy01AsImage(cls, filepath, numpy01):
        np.clip(numpy01, 0, 1, out=numpy01)
        imageio.imwrite(filepath, (numpy01 * 255).astype(np.uint8))

    #     if len(numpy01.shape) == 3 and numpy01.shape[2] == 4:  # RGBA
    #         cls._savePngRGBA(filepath, numpy01, "RGBA")
    #     elif len( numpy01.shape) == 3 and numpy01.shape[2] == 3: # RGB
    #         cls._savePngRGB(filepath, numpy01, "RGB")
    #     else:  # Scalar (grayscale)
    #         cls._savePngScalar(filepath, numpy01)
    #
    # @classmethod
    # def _savePngRGBA(cls, filepath, numpy01, pixelFormat="RGBA"):
    #     print("_savePngRGBA")
    #     print(numpy01)
    #     idx_r = pixelFormat.upper().find('R')
    #     idx_g = pixelFormat.upper().find('G')
    #     idx_b = pixelFormat.upper().find('B')
    #     idx_a = pixelFormat.upper().find('A')
    #
    #     # reorder channels
    #     rows = numpy01.shape[0]
    #     cols = numpy01.shape[1]
    #     rgba = np.zeros((rows, cols, 4), 'float')
    #     rgba[..., 0] = numpy01[..., idx_r]  # R
    #     rgba[..., 1] = numpy01[..., idx_g]  # G
    #     rgba[..., 2] = numpy01[..., idx_b]  # B
    #     rgba[..., 3] = numpy01[..., idx_a]  # A
    #
    #     f = open(filepath, 'wb')  # binary mode is important
    #     w = png.Writer(cols, rows, greyscale=False, alpha=True)
    #     w.write(f, np.reshape(rgba * 255, (-1, cols * 4)))
    #     f.close()
    #
    #
    # @classmethod
    # def _savePngRGB(cls, filepath, numpy01, pixelFormat="RGB"):
    #     print("_savePngRGB")
    #     idx_r = pixelFormat.upper().find('R')
    #     idx_g = pixelFormat.upper().find('G')
    #     idx_b = pixelFormat.upper().find('B')
    #
    #     # reorder channels
    #     rows = numpy01.shape[0]
    #     cols = numpy01.shape[1]
    #     rgb = np.zeros((rows, cols, 3), 'float')
    #     rgb[..., 0] = numpy01[..., idx_r]  # R
    #     rgb[..., 1] = numpy01[..., idx_g]  # G
    #     rgb[..., 2] = numpy01[..., idx_b]  # B
    #
    #     f = open(filepath, 'wb')  # binary mode is important
    #     w = png.Writer(cols, rows, greyscale=False, alpha=False)
    #     w.write(f, np.reshape(rgb * 255, (-1, cols * 3)))
    #     f.close()
    #
    #     # print filepath, rgba, idx_r, idx_g, idx_b, idx_a
    #
    # @staticmethod
    # def _savePngScalar(filepath, numpy01):
    #     rows = numpy01.shape[0]
    #     cols = numpy01.shape[1]
    #     f = open(filepath, 'wb')  # binary mode is important
    #     w = png.Writer(cols, rows, greyscale=True, alpha=False)
    #     w.write(f, np.reshape(numpy01 * 255, (-1, cols)))
    #     f.close()

    @classmethod
    def loadImageAsNumpy01Rgba(cls, filepath, size=None):
        """ returns always 4 channel pixmap """

        # FIXME: better use scipy.misc.imread() ... does it load alpha?
        try:
            # im = scipy.misc.imread( filepath) / 255.0
            im = imageio.imread(filepath) / 255.0
        except IOError as e:
            print("error loading image file %s:\nmsg: %s" % (filepath, str(e)))
            raise e
        # print "shape of loaded image: ", im.shape

        if len(im.shape) == 2:  # grayscale
            alpha = np.ones(im.shape[:2])
            im = np.dstack((im, im, im, alpha))
        elif im.shape[2] == 4:  # rgba
            pass
        elif im.shape[2] == 3:  # rgb
            im = UtilMap.rgb2rgba(im)

        if size:
            return UtilCanvas.resize2017(im.astype(np.float), size)
        else:
            return im.astype(np.float)

    @classmethod
    def loadImageAsNumpy01Rgb(cls, filepath, size=None):
        """
        03/2018
        returns always 3 channel pixmap
        """
        try:
            im = imageio.imread(filepath) / 255.0
        except IOError as e:
            print("error loading image file %s:\nmsg: %s" % (filepath, str(e)))
            raise e

        if len(im.shape) == 2:  # grayscale
            im = np.dstack((im, im, im))
        elif im.shape[2] == 3:  # rgb
            pass
        elif im.shape[2] == 4:  # rgba
            r = im[:, :, 0]
            g = im[:, :, 1]
            b = im[:, :, 2]
            im = np.dstack((r, g, b))

        if size:
            return UtilCanvas.resize2017(im.astype(np.float), size)
        else:
            return im.astype(np.float)


    @classmethod
    def loadImageAsNumpy01Scalar(cls, filepath, size=None):
        """ returns 1 channel scalar map """
        im = cls.loadImageAsNumpy01Rgba(filepath)
        scalar01 = im[:, :, 0] * 0.2125 + im[:, :, 1] * 0.7154 + im[:, :, 2] * 0.0721
        if size:
            return UtilCanvas.resize2017(scalar01, size)
        else:
            return scalar01

