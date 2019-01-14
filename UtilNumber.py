#
# 01/2018
#
from GenArt.AbstractObject import AbstractObject


class UtilNumber(AbstractObject):

    @staticmethod
    def clip01(num):
        return min(1.0, max(0.0, num))



    @staticmethod
    def sign11(x):
        return (1, -1)[x < 0]

