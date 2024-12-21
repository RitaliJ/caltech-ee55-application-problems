import PIL.Image
import PIL.ImageShow
import numpy as np
import PIL
from numpy import random

boat_tiff = PIL.Image.open('./boat.tiff') 
image_array = np.array(boat_tiff)

print(f'{len(image_array)}, {len(image_array[0])}')

def quantize_img(img_arr):
    quantized_image_arr = np.array([[0 if val < 127 else 255 for val in row] 
                                    for row in img_arr])
    quantized_img = PIL.Image.fromarray(quantized_image_arr.astype('uint8'))
    quantized_img.show()

quantize_img(image_array)

def noisy_img_vectors(image_array, var):
    noise = random.normal(0, var, (len(image_array), len(image_array[0])))
    return np.add(image_array, noise)

variances = [0.5, 5, 50]
# for var in variances:
#     quantize_img(noisy_img_vectors(image_array, var))
    

