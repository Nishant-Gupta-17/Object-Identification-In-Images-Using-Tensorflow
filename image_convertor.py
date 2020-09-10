# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:44:35 2017

@author: NISHANT
"""

import os
from PIL import Image
actual_image_path = "C:/Users/NISHANT/Desktop/final/peepal"
image_files = os.listdir(actual_image_path)
processed_image = "C:/Users/NISHANT/Desktop/final/ppal"
os.chdir(actual_image_path)
count = 0
for image in image_files:
    im = Image.open(image)
    im = im.resize((50,50,))
    im.save(processed_image + '/image' + str(count) + '.jpg')
    count += 1
    