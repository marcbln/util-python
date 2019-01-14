# 06/2018 created


from subprocess import call

from McxUtil.UtilCanvas import UtilCanvas


class UtilSvg:

    @classmethod
    def renderSvg(cls, pathSrcSvg: str, pathDestPng: str):
        (width, height) = UtilCanvas.getCanvasSizeInt()
        call(["/usr/bin/inkscape", "-z", "-e", pathDestPng, "-w", str(width), "-h", str(height), pathSrcSvg])
        # alternative: exec("/usr/bin/convert $pathSrcSvg -resize 500x500 $pathDestPng");

