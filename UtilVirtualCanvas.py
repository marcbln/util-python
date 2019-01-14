#
# 01/2018
#

from GenArt.AbstractObject import AbstractObject
from GenArt.DataTypes.COLOR import COLOR
from McxUtil.UtilDrawRgba import UtilDrawRgba
from McxUtil.UtilUnit import UtilUnit
from RoboPainter.Line2D import Line2D


# ALL POSITIONS AND LENGTHS ARGUMENTS ARE IN MM

class UtilVirtualCanvas(AbstractObject):


    @classmethod
    def drawRect(cls, npMapRgba, p1, p2, p3, p4, color: COLOR):
        UtilDrawRgba.drawRect(npMapRgba, p1.mm2pxInt(), p2.mm2pxInt(), p3.mm2pxInt(), p4.mm2pxInt(), color)

    @classmethod
    def drawCircle(cls, npMapRgba, center, radius, color: COLOR):
        UtilDrawRgba.drawCircle(npMapRgba, center.mm2pxInt(), UtilUnit.mm2px(radius), color)



    @classmethod
    def drawTriangle(cls, npMapRgba, p1, p2, p3, color: COLOR):
        UtilDrawRgba.drawTriangle(npMapRgba, p1.mm2pxInt(), p2.mm2pxInt(), p3.mm2pxInt(), color)














    @classmethod
    def drawLineString(cls, virtualCanvas, points, diameterMm, color: COLOR):
        for idx in range(1, len(points)):
            p1 = points[idx - 1]
            p2 = points[idx]
            centerLine = Line2D(p1, p2)
            topLine = centerLine.getParallel(diameterMm / 2)
            bottomLine = centerLine.getParallel(-diameterMm / 2)
            cls.drawRect(virtualCanvas, topLine.p1, topLine.p2, bottomLine.p2, bottomLine.p1, color)
            cls.drawCircle(virtualCanvas, p1, diameterMm / 2, color)
        cls.drawCircle(virtualCanvas, p2, diameterMm / 2, color)

    @classmethod
    def drawLine(cls, virtualCanvas, p1, p2, diameterMm, color: COLOR):
        if(p1 != p2):
            centerLine = Line2D(p1, p2)
            topLine = centerLine.getParallel(diameterMm / 2)
            bottomLine = centerLine.getParallel(-diameterMm / 2)
            cls.drawRect(virtualCanvas, topLine.p1, topLine.p2, bottomLine.p2, bottomLine.p1, color)
            cls.drawCircle(virtualCanvas, p1, diameterMm / 2, color)
        cls.drawCircle(virtualCanvas, p2, diameterMm / 2, color)
