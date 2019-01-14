import numpy
from scipy import ndimage


class UtilWarp:
    
    
    
    @staticmethod
    def warpByDelta( srcMap, dx, dy, mode):
        """ sollte mit verschiedenen MAP_XXX-Typen funktionieren """

#         try: # fails if dx / dy are integers
#             print "warpByDelta / srcMap.shape, dx.shape, dy.shape: ", srcMap.shape, dx.shape, dy.shape
#         except: 
#             pass


        width = srcMap.shape[1]
        height = srcMap.shape[0]
        
        # FIXME: dtype sollte irgendwo global eingestellt werden
        # FIXME: use meshgrid??!!
        px = numpy.array( [ [ j for j in range(width)] for i in range(height)], dtype=numpy.float64)
        py = numpy.array( [ [ i for j in range(width)] for i in range(height)], dtype=numpy.float64)
    
        px += dx
        py += dy

        return UtilWarp._warp( srcMap, px, py, mode)
    
    @staticmethod
    def warpByCoordinates( srcMap, coordinatesX, coordinatesY, mode):
        """ sollte mit verschiedenen MAP_XXX-Typen funktionieren """

#         height = srcMap.shape[0]
#         width = srcMap.shape[1]
   
        return UtilWarp._warp( srcMap, coordinatesX, coordinatesY, mode)
    
    
    
    
    
    @staticmethod
    def _warp( srcMap, coordinatesX, coordinatesY, mode, order=1):
        
        coordinate_array = numpy.array([coordinatesY, coordinatesX])

        # map_scalar
        if len( srcMap.shape) == 2:
            return ndimage.map_coordinates( srcMap, coordinate_array, order=order, mode=mode)
        
        
        # map_pixels, map_vec2d, map_scalar(?) etc..
        rgbArray = numpy.zeros( srcMap.shape, 'float')
        for idx in range( srcMap.shape[2]):
            warped_tmp = ndimage.map_coordinates( srcMap[..., idx], coordinate_array, order=order, mode=mode)
            rgbArray[..., idx] = warped_tmp
        
        return rgbArray        
    
    
    
    
    
    
    
    
    
    