import numpy

from GenArt.AbstractObject import AbstractObject


# see http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
# see http://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing
class UtilNormalize(AbstractObject):

    @staticmethod
    def normalize(map):
        """
        normalizes the passed array
        actually is is not normalizing but min-max-scaling between 0 and 1 (TODO rename)
        """
        min_ = numpy.min( map)
        max_ = numpy.max( map)
        if max_ > min_:
            map -= min_
            map /= (max_-min_)

        return map

    @staticmethod
    def normalizeCopy( mapScalar):
        """
         returns a newly created numpy array with normalized values
         actually is is not normalizing but min-max-scaling between 0 and 1 (TODO rename)
        """
        min_ = numpy.min(mapScalar)
        max_ = numpy.max(mapScalar)
        resNorm = (mapScalar - min_) / (max_-min_)
        return resNorm
