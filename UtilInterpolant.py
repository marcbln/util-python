from __future__ import division

import numpy

# OLD:
# def generateNLevelInterpolant1D1D( nSteps, smoothFactor):
#     y = numpy.arange(0, nSteps, 1)
#     y = numpy.repeat(y, 2) # [0 0 1 1 2 2 ...]
#
#
#     dist = 1.0 / (nSteps)
#     gradientWidth = dist * smoothFactor
#     print dist
#     print gradientWidth
#     t = [0]
#     for i in range(1,nSteps):
#         t.append( i*dist - gradientWidth/2.0)
#         t.append( i*dist + gradientWidth/2.0)
#     t.append( 1)
#
#     print y, t
#     return INTERPOLANT_1D_1D( 'linear', t, y)
from GenArt.DataTypes.INTERPOLANT_1D_1D import INTERPOLANT_1D_1D


class UtilInterpolant:

    @staticmethod
    def generateStepFunction1D1D( nSteps, smoothFactor01):
        y = numpy.arange(0, nSteps, 1)
        y = numpy.repeat(y, 2) # [0 0 1 1 2 2 ...]

    #    print "nSteps", nSteps
        nGradients = nSteps - 1
    #    print "nGradients", nGradients

        lengthAllGradients = smoothFactor01
    #    print "lengthAllGradients", lengthAllGradients

        lengthGradient = lengthAllGradients / nGradients
    #    print "lengthGradient", lengthGradient

        lengthAllLevels = 1.0 - lengthAllGradients
    #    print "lengthAllLevels", lengthAllLevels

        lengthLevel = lengthAllLevels / nSteps
    #    print "lengthLevel", lengthLevel

        t = [ 0.0 ]
        pos = 0.0
        for i in range(1,nSteps):
            pos += lengthLevel
            t.append( pos)
            pos += lengthGradient
            t.append( pos)
        t.append( 1.0)
        #print t
        #print y/(nSteps-1)
        return INTERPOLANT_1D_1D( 'linear', t, y/(nSteps-1) )







    # # FIXME: add two extra points per level, otherwise the level is not constant
    # def generateNLevelQuadraticInterpolant1D1D( nSteps, smoothFactor01):
    # #    print "nSteps", nSteps
    #     nGradients = nSteps - 1
    # #    print "nGradients", nGradients
    #
    #     lengthAllGradients = smoothFactor01
    # #    print "lengthAllGradients", lengthAllGradients
    #
    #     lengthGradient = lengthAllGradients / nGradients
    # #    print "lengthGradient", lengthGradient
    #
    #     lengthAllLevels = 1.0 - lengthAllGradients
    # #    print "lengthAllLevels", lengthAllLevels
    #
    #     lengthLevel = lengthAllLevels / nSteps
    # #    print "lengthLevel", lengthLevel
    #
    #     t = [0]
    #     y = [0]
    #     posY = 0
    #     posT = 0.0
    #     for i in range(1,nSteps):
    #         # T...
    #         posT += lengthLevel
    #         t.append( posT)
    #
    #         posT += lengthGradient / 2.0
    #         t.append( posT)
    #
    #         posT += lengthGradient / 2.0
    #         t.append( posT)
    #
    #         # Y ...
    #         y.append( posY)
    #         y.append( posY + 0.5)
    #         y.append( posY + 1)
    #         posY += 1
    #
    #     t.append( 1)
    #     y.append( posY)
    #
    #     print t
    #     print y
    #
    #     return INTERPOLANT_1D_1D( 'quadratic', t, y)
