#
# 03/2018
# ALL POSITIONS AND LENGTHS ARGUMENTS ARE IN PX
#

import numpy as np
from skimage.draw import draw

from GenArt.AbstractObject import AbstractObject


class UtilDrawGeneric(AbstractObject):

    @classmethod
    def drawTriangle(cls, npMapRgb, p1, p2, p3, pixel):
        """ 01/2018 """
        npCoordinatesPx = np.array((p1, p2, p3))
        rr, cc = draw.polygon(npCoordinatesPx[:, 1], npCoordinatesPx[:, 0], npMapRgb.shape[:2])
        npMapRgb[rr, cc] = pixel


    @classmethod
    def drawCircle(cls, npMapRgba, center, radius, pixel):
        """ 01/2018 """
        rr, cc = draw.circle(center[1], center[0], radius, npMapRgba.shape[:2])
        #print("rr", rr.shape)
        #print("npMapRgba", npMapRgba.shape)
        npMapRgba[rr, cc] = pixel


    @classmethod
    def drawRect(cls, npMapRgba, p1, p2, p3, p4, pixel):
        """ 01/2018 """
        npCoordinatesPx = np.array((p1, p2, p3, p4))
        rr, cc = draw.polygon(npCoordinatesPx[:, 1], npCoordinatesPx[:, 0], npMapRgba.shape[:2])
        npMapRgba[rr, cc] = pixel




    @classmethod
    def getPixel(cls, npMapRgba, pos):
        """ 03/2018 """
        return npMapRgba[pos[0], pos[1]] ## TODO: check if order x, y is correct
