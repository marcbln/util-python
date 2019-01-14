# 06/2018 copied from push3 to here

import numpy

# http://stackoverflow.com/a/3375291/190597
# http://stackoverflow.com/a/9166671/190597


class UtilComposite:


    @staticmethod
    def compositeWithMask(src, dst, src_opacity):
        """ does use alpha channel of src for blending ... non premultiplied """

        rgb = numpy.index_exp[:, :, :3]
        alpha = numpy.index_exp[:, :, 3:]


        src_a = ( src[alpha].transpose(2,0,1) * src_opacity ).transpose( 1,2,0)
        src_rgb = src[rgb]

        dst_a = dst[alpha]
        dst_rgb = dst[rgb]

        out_a = src_a + dst_a * (1-src_a)

#        if out_a == 0:
#            out_rgb = numpy.array([0,0,0])
#        else:

        out_rgb = (src_rgb * src_a + dst_rgb * dst_a * (1-src_a)) / out_a
        out_rgb = numpy.nan_to_num(out_rgb) # nan->0 # => if out_a == 0, then out_rgb = 0

        #out = numpy.empty_like(src.shape)
        out = numpy.empty(src.shape, dtype = 'float')

        # out_a = src_a + dst_a * (1-src_a)
        #print out_rgb
        out[rgb] = out_rgb
        out[alpha] = out_a
        return out
    
    

    @staticmethod
    def alpha_composite_non_premultiplied(src, src_opacity, dst):
        out = numpy.empty(src.shape, dtype = 'float')
        alpha = numpy.index_exp[:, :, 3:]
        rgb = numpy.index_exp[:, :, :3]
        src_a = src[alpha] * src_opacity
        dst_a = dst[alpha]
        
        src_rgb = src[rgb] * src_opacity
        dst_rgb = dst[rgb]
        
        out[alpha] = src_a+dst_a*(1-src_a)
    #    old_setting = numpy.seterr(invalid = 'ignore')
        out[rgb] = (src_rgb * src_a + dst_rgb*dst_a*(1-src_a))/out[alpha] # FIXME: errors if alpha is zero ..
    #    numpy.seterr(**old_setting)
    #    print numpy.count_nonzero( numpy.isnan(out[:,:,1]))
    #    print numpy.count_nonzero( src[:,:,3])
    #    print numpy.count_nonzero( dst[:,:,3])
        return out
    
    
    



#
#     @staticmethod
#     def composite_premultiplied_with_mask(src, dst, mask):
#         """ does NOT use alpha channel of src for blending """
#         out = (src.transpose(2,0,1)*mask + dst.transpose(2,0,1)*(1-mask)).transpose(1,2,0)
#         return out
#


    
    # 
    # def alpha_composite_premultiplied(src, src_opacity, dst):
    #     out = numpy.empty(src.shape, dtype = 'float')
    #     rgb = numpy.index_exp[:, :, :3]
    #     alpha = numpy.index_exp[:, :, 3:]
    #     src_a = src[alpha] * src_opacity
    #     dst_a = dst[alpha]
    #     src_rgb = src[rgb] * src_opacity
    #     dst_rgb = dst[rgb]
    #     out[rgb] = src_rgb + dst_rgb * (1-src_a)
    #     out[alpha] = src_a + dst_a*(1-src_a)
    #     return out
    
#     @staticmethod
#     def alpha_composite_premultiplied_with_mask(src, dst, src_opacity):
#         """ does use alpha channel of src for blending """
#
#         rgb = numpy.index_exp[:, :, :3]
#         alpha = numpy.index_exp[:, :, 3:]
#
#         out = numpy.empty(src.shape, dtype = 'float')
#
#         src_a = ( src[alpha].transpose(2,0,1) * src_opacity ).transpose( 1,2,0)
#         src_rgb = ( src[rgb].transpose(2,0,1) * src_opacity ).transpose(1,2,0)
#
#         dst_a = dst[alpha]
#         dst_rgb = dst[rgb]
#
#         out[rgb] = src_rgb + dst_rgb * (1-src_a)
#         out[alpha] = src_a + dst_a * (1-src_a)
#
#         return out


