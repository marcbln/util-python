"""
 *       paper sizes
 *       -----------
 *       A3    297 x 420 mm
 *       A4    210 x 297 mm
 *       A5    148 x 210 mm
 *       A6    105 x 148 mm
 *
"""

import math

import numpy as np
from skimage.transform import resize

# 12/2017: in push3 this was UtilFixSize
from GenArt.DataTypes.Path2d.Vector2d import Vector2d


class UtilCanvas:
    _canvasSize = None

    @classmethod
    def setCanvasSize(cls, size):
        cls._canvasSize = size

    @classmethod
    def getCanvasSize(cls):
        return cls._canvasSize

    @classmethod
    def getShapeMapScalar(cls):
        """ this on is for xy """
        canvasWidth, canvasHeight = cls.getCanvasSizeInt()
        return (canvasHeight, canvasWidth)

    @classmethod
    def getShapeMapPixel(cls):
        """ this on is for xy """
        canvasWidth, canvasHeight = cls.getCanvasSizeInt()
        return (canvasHeight, canvasWidth, 4)

    @classmethod
    def getCanvasSizeInt(cls):
        canvasWidth, canvasHeight = map(int, cls._canvasSize.split('x'))
        return (canvasWidth, canvasHeight)

    @classmethod
    def getCanvasSizeVector2d(cls):
        canvasWidth, canvasHeight = map(int, cls._canvasSize.split('x'))
        return Vector2d(canvasWidth, canvasHeight)

    @classmethod
    def getCanvasCenterVector2d(cls):
        canvasWidth, canvasHeight = map(int, cls._canvasSize.split('x'))
        return Vector2d(canvasWidth, canvasHeight) / 2.0

    @classmethod
    def getCanvasWidth(cls):
        canvasWidth, canvasHeight = map(int, cls._canvasSize.split('x'))
        return canvasWidth

    @classmethod
    def getCanvasHeight(cls):
        canvasWidth, canvasHeight = map(int, cls._canvasSize.split('x'))
        return canvasHeight

    # 12/2017
    @classmethod
    def resizeToCanvasSize(cls, mapPixelOrMapscalar):
        """
        resizes the map to canvasSize
        """
        resized = cls.resize2017(mapPixelOrMapscalar, cls._canvasSize)
        return resized

    # 12/2017 copied from push v3
    @staticmethod
    def calculateCanvasSize(aspectRatio, megaPixel):
        """
        calculates canvas size in px, given an aspect ratio and a MP

        :param string aspectRatio: eg "16:9"
        :param float megaPixel: eg 0.3
        :return string canvasSize: eg: 730x410
        """
        arWidth, arHeight = map(float, aspectRatio.split(':'))
        arArea = arWidth * arHeight
        pixels = megaPixel * 1000000.0
        scale = math.sqrt(pixels / arArea)
        canvasSize = "%dx%d" % (round(arWidth * scale), round(arHeight * scale))
        return canvasSize

    # still needed in 2018?
    @staticmethod
    def maxSize(npArray01, maxW, maxH):
        """ TODO: remove this """
        w = npArray01.shape[1]
        h = npArray01.shape[0]

        # nothing
        if w <= maxW and h <= maxH:
            return npArray01

        r_in = float(w) / h
        r_max = float(maxW) / maxH

        if r_in > r_max:
            new_w = maxW
            new_h = int(round(new_w / r_in))
        else:
            new_h = maxH
            new_w = int(round(new_h * r_in))

        # print "maxSize: %d/%d -> %d/%d" % (w, h, new_w, new_h)

        if len(npArray01.shape) == 2:  # grayscale
            return UtilCanvas.downsampleMapScalar(npArray01, new_w, new_h)
        elif len(npArray01.shape) == 3 and npArray01.shape[2] == 4:
            return UtilCanvas.downsampleRGBA(npArray01, new_w, new_h)

        raise Exception("don't know how to handle numpy with shape %s" % npArray01.shape)

    @classmethod
    def resize2017(cls, npArray01, destSize):
        """ 12/2017 version """
        widthDest, heightDest = map(int, destSize.split('x'))
        (heightSrc, widthSrc) = npArray01.shape[:2]
        aspectRatioSrc = widthSrc / heightSrc
        aspectRatioDest = widthDest / heightDest
        # print("aspectRatioSrc =  widthSrc / heightSrc = " + str(aspectRatioSrc))
        # print("aspectRatioDest = " + str(aspectRatioDest))
        cropLeft = 0
        cropRight = 0
        cropTop = 0
        cropBottom = 0
        if aspectRatioSrc > aspectRatioDest:
            # print("cropX (crop left + right)")
            sf = heightSrc / heightDest
            cropX = widthSrc - sf * widthDest
            cropLeft = cropRight = int(round(cropX / 2))
        elif aspectRatioSrc < aspectRatioDest:
            # print("cropY (crop top + bottom)")
            # print("heightDest:", heightDest)
            # print("widthDest:", widthDest)
            # print("heightSrc:", heightSrc)
            # print("widthSrc:", widthSrc)
            sf = widthSrc / widthDest
            cropY = heightSrc - sf * heightDest
            cropTop = cropBottom = int(round(cropY / 2))
            # print( "sf", sf)
            # print( "cropY", cropY)
        # TODO later: add antialiasing (in 01/2018 it is not in library): return resize( npArray01[cropTop:heightSrc-cropBottom, cropLeft:widthSrc-cropRight, ...], (heightDest, widthDest), mode='edge', anti_aliasing=True)
        return resize(npArray01[cropTop:heightSrc - cropBottom, cropLeft:widthSrc - cropRight, ...],
                      (heightDest, widthDest), mode='edge')

    # @staticmethod
    # def __resize( npArray01, newWidth, newHeight):
    #     """ uses skimage """
    #     ret = resize( npArray01, (newHeight, newWidth), mode='constant')
    #     return ret
    #
    # @staticmethod
    # def __resize2( npArray01, newWidth, newHeight, interp):
    #     """ uses scipy """
    #     """ interp: Interpolation to use for re-sizing ('nearest', 'bilinear', 'bicubic' or 'cubic') """
    #     ret  = imresize( npArray01, (newHeight, newWidth), interp) / 255.0
    #     return ret

    @staticmethod
    def downsampleRGBA(rgba, newWidth, newHeight):
        """ for pixelize etc... """
        # print "downsample to: %d x %d" % (shapeX, shapeY)
        height = rgba.shape[0]
        width = rgba.shape[1]

        lsX = np.round(np.linspace(0, width, newWidth + 1)).astype(int)
        lsY = np.round(np.linspace(0, height, newHeight + 1)).astype(int)
        # print lsX, lsY
        ret = np.empty(shape=[newHeight, newWidth, 4])
        for idxX in range(len(lsX) - 1):
            xFrom = lsX[idxX]
            xTo = lsX[idxX + 1]
            for idxY in range(len(lsY) - 1):
                yFrom = lsY[idxY]
                yTo = lsY[idxY + 1]
                area = (yTo - yFrom) * (xTo - xFrom)
                pixelsum = np.sum(np.sum(rgba[yFrom:yTo, xFrom:xTo, :], axis=0), axis=0)
                ret[idxY, idxX] = pixelsum / area
        return ret

    @staticmethod
    def downsampleMapScalar(mapScalar, newWidth, newHeight):
        """ eg. for Gradients, antialiasing(render highres, then downsample)
            if used for AA, then width/height should be N*shapeX/Y where n is a Natural Number.
            in this case, the algorithm could be optimized: strides?, a single numpy-div
        """

        # print "downsample to: %d x %d" % (shapeX, shapeY)
        height, width = mapScalar.shape

        lsX = np.round(np.linspace(0, width, newWidth + 1)).astype(int)
        lsY = np.round(np.linspace(0, height, newHeight + 1)).astype(int)
        # print lsX, lsY
        ret = np.empty(shape=[newHeight, newWidth])
        for idxX in range(len(lsX) - 1):
            xFrom = lsX[idxX]
            xTo = lsX[idxX + 1]
            for idxY in range(len(lsY) - 1):
                yFrom = lsY[idxY]
                yTo = lsY[idxY + 1]
                area = (yTo - yFrom) * (xTo - xFrom)
                pixelsum = np.sum(np.sum(mapScalar[yFrom:yTo, xFrom:xTo], axis=0), axis=0)
                ret[idxY, idxX] = pixelsum / area
        return ret

    #     @staticmethod
    #     def zoom( npArray01, factor, order=0):
    #         """ order : 0 - nearest,
    #                     1 - bilinear
    #                     2 - cubic
    #         """
    #         return scipy.ndimage.zoom( npArray01, factor, order=0)

    @classmethod
    def create4Ch(cls):
        """
        numpy array is returned
        TODO: return white transparent canvas?
        """
        return np.zeros((cls.getCanvasHeight(), cls.getCanvasWidth(), 4))

    @classmethod
    def create3Ch(cls):
        """
        numpy array is returned
        """
        return np.zeros((cls.getCanvasHeight(), cls.getCanvasWidth(), 3))

    @classmethod
    def getCanvasDiagonal(cls):
        return math.sqrt(cls.getCanvasWidth() ** 2 + cls.getCanvasHeight() ** 2)

    @classmethod
    def getVector2dOnCanvas(cls, x01, y01):
        (w, h) = cls.getCanvasSizeInt()
        return Vector2d(w * x01, h * y01)
