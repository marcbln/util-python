
# 03/2018 .. tools for converting rgb / rgba and stuff
import numpy as np


class UtilMap:

    #
    # 03/2018
    #
    @staticmethod
    def rgb2rgba(im):
        alpha = np.ones(im.shape[:2])
        return np.dstack((im[:, :, 0], im[:, :, 1], im[:, :, 2], alpha))
