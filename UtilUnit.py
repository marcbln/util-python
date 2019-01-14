"""
 *       paper sizes
 *       -----------
 *       A3    297 x 420 mm
 *       A4    210 x 297 mm
 *       A5    148 x 210 mm
 *       A6    105 x 148 mm
 *
"""


class UtilUnit:
    ONE_INCH_IN_MM = 25.4  # 1 inch = 25.4 mm

    @classmethod
    def px2mm(cls, px, dpi=96):
        onePxInMm = cls.ONE_INCH_IN_MM / dpi
        return onePxInMm * px

    @classmethod
    def mm2px(cls, mm, dpi=96):
        onePxInMm = cls.ONE_INCH_IN_MM / dpi
        return mm / onePxInMm

    @classmethod
    def px2pt(cls, px, dpi=96):
        """
        * There are 72 points per inch; if it is sufficient to assume 96 pixels per inch, the formula is rather simple:
        * points = pixels * 72 / 96
                   * The W3C has defined the pixel measurement px as exactly 1/96th of 1in regardless of the actual resolution of your display, so the above formula should be good for all web work.
        """
        return px * 72 / dpi

    @classmethod
    def mm2pxInt(cls, mm, dpi=96):
        return int(round(cls.mm2px(mm, dpi)))
