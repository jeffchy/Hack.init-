import os
 
def CompressImage(image_name,max_size):
       image_stat = os.stat(image_name)
       image_size = image_stat.st_size / 4.0
       if image_size > max_size:
              compress_factor = max_size / image_size * 100
              print("compressing %s" % image_name)
              os.system("convert %s -quality %s %s" %(image_name,compress_factor,image_name))
             
def CompressAll():
       ext_names = ['.JPG','.jpg','.jepg']
       for each_image in os.listdir('./'):
              for ext_name in ext_names:
                     if each_image.endswith(ext_name):
                            CompressImage(each_image,1200)
                            break
CompressAll()