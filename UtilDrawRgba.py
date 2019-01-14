#
# 01/2018
#
import numpy as np
from GenArt.AbstractObject import AbstractObject
from GenArt.DataTypes.COLOR import COLOR
from skimage.draw import draw


# ALL POSITIONS AND LENGTHS ARGUMENTS ARE IN PX


class UtilDrawRgba(AbstractObject):

    SET_PIXEL_MODE_REPLACE = 'REPLACE'


    # TODO: slooow ..
    @classmethod
    def setPixel(cls, npMapRgba, posX, posY, rgb_a, alpha_a):
        """ see https://en.wikipedia.org/wiki/Alpha_compositing """
        red_b, green_b, blue_b, alpha_b = npMapRgba[posY, posX]
        rgb_b_premultiplied = np.multiply((red_b, green_b, blue_b), alpha_b)
        rgb_a_premultiplied = np.multiply(rgb_a, alpha_a)
        # out
        rgb_o = rgb_a_premultiplied + np.multiply(rgb_b_premultiplied, (1 - alpha_a))
        alpha_o = alpha_a + alpha_b * (1 - alpha_a)
        npMapRgba[posY, posX] = [rgb_o[0], rgb_o[1], rgb_o[2], alpha_o]

    @classmethod
    def setPixels(cls, npMapRgba, cc, rr, rgb_a, alpha_a):
        """ see https://en.wikipedia.org/wiki/Alpha_compositing """
        # 1) premultiply with alpha
        npMapRgba[rr, cc, 0] *= npMapRgba[rr, cc, 3] * (1 - alpha_a)
        npMapRgba[rr, cc, 1] *= npMapRgba[rr, cc, 3] * (1 - alpha_a)
        npMapRgba[rr, cc, 2] *= npMapRgba[rr, cc, 3] * (1 - alpha_a)
        # 2) premultiply given color
        rgb_a_premultiplied = np.multiply(rgb_a, alpha_a)
        # 3) composite
        npMapRgba[rr, cc, 0] += rgb_a_premultiplied[0]
        npMapRgba[rr, cc, 1] += rgb_a_premultiplied[1]
        npMapRgba[rr, cc, 2] += rgb_a_premultiplied[2]
        # alpha
        npMapRgba[rr, cc, 3] *= (1 - alpha_a)
        npMapRgba[rr, cc, 3] += alpha_a

    @classmethod
    def drawRect(cls, npMapRgba, p1, p2, p3, p4, color: COLOR):
        """ 01/2018 """
        npCoordinatesPx = np.array((p1, p2, p3, p4))
        rr, cc = draw.polygon(npCoordinatesPx[:, 1], npCoordinatesPx[:, 0], npMapRgba.shape[:2])
        npMapRgba[rr, cc] = color.getRGBA()

    @classmethod
    def drawCircle(cls, npMapRgba, centerX, centerY, radius, color: COLOR, alpha=1.0, setPixelMode=SET_PIXEL_MODE_REPLACE):
        """ 01/2018 """
        # radiusPx = UtilUnit.mm2px(radius)
        rr, cc = draw.circle(centerX, centerY, radius, npMapRgba.shape[:2])
        cls.setPixels(npMapRgba, cc, rr, color.getRGB(), alpha)
        #npMapRgba[rr, cc] = color.getRGBA()
