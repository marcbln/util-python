import numpy as np
import scipy.ndimage.filters as filters


# 03/2018

class UtilImageFilter:


    @classmethod
    def maximum_filter2d(cls, image, neighborhood_size):
        if len(image.shape) == 2:
            return filters.maximum_filter(image, neighborhood_size)
        else:
            ret = np.zeros(image.shape)
            for idx in range(image.shape[2]):
                ret[...,idx] = filters.maximum_filter(image[...,idx], neighborhood_size)
            return ret


    @classmethod
    def minimum_filter2d(cls, image, neighborhood_size):
        if len(image.shape) == 2:
            return filters.minimum_filter(image, neighborhood_size)
        else:
            ret = np.zeros(image.shape)
            for idx in range(image.shape[2]):
                ret[...,idx] = filters.minimum_filter(image[...,idx], neighborhood_size)
            return ret

