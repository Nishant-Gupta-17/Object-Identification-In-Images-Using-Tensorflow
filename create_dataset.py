# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:40:54 2017

@author: NISHANT
"""

import os
import numpy as np
import pickle 
from scipy import ndimage
import matplotlib.pyplot as plt

folder = "pguns"
path = "C:/Users/NISHANT/Desktop/final/"
os.chdir(path + folder)
train_dataset = np.ndarray(shape = (1300,7500),dtype = np.uint8)
count = 0
for i in range(1300):
    im = ndimage.imread('image'+ str(i) + '.jpg')
    if len(im.shape) != 3:
        continue
    im = im.reshape((7500))
    train_dataset[count,:] = im
    count += 1
for i in range(1299,0,-1):
    if sum(train_dataset[i]) < 1:
        train_dataset =np.delete(train_dataset, i, axis=0)
    else:
        break
train_label = np.zeros(train_dataset.shape[0])

test_dataset = np.ndarray(shape = (234,7500),dtype = np.uint8)
test_count = 0
for i in range(1300,1534):
    im = ndimage.imread('image'+ str(i) + '.jpg')
    if len(im.shape) != 3:
        continue
    im = im.reshape((7500))
    test_dataset[test_count,:] = im
    test_count += 1
i=test_dataset[0].reshape((50,50,3))
plt.imshow(i)
plt.show()

for i in range(233,0,-1):
    if sum(test_dataset[i]) < 1:
        test_dataset =np.delete(test_dataset, i, axis=0)
    else:
        break
test_label = np.zeros(test_dataset.shape[0])
os.chdir(path)
f = open('pguns.pickle', 'wb')
data = {'train_data':train_dataset, 
        'train_label':train_label,
        'test_data':test_dataset, 
        'test_label':test_label} 
pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
f.close()