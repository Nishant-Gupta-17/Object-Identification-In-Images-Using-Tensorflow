# -*- coding: utf-8 -*-
# @Author: NISHANT
# @Date:   2017-02-12 23:01:23
# @Last Modified by:   NISHANT
# @Last Modified time: 2017-02-13 00:49:27

import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import pickle

data_file = open('pguns.pickle', 'rb')
pguns_data = pickle.load(data_file)
train_data1 = pguns_data['train_data']
train_labels1 = pguns_data['train_label']
test_data1 = pguns_data['test_data']
test_label1 = pguns_data['test_label']

data_file = open('ppal.pickle', 'rb')
ppal_data = pickle.load(data_file)
train_data2 = ppal_data['train_data']
train_labels2 = ppal_data['train_label']
test_data2 = ppal_data['test_data']
test_label2 = ppal_data['test_label']

train_data = np.concatenate((train_data1, train_data2), axis=0)
train_labels = np.concatenate((train_labels1, train_labels2), axis=0)

test_data = np.concatenate((test_data1, test_data2), axis=0)
test_labels = np.concatenate((test_label1, test_label2), axis=0)

def randomise(train, label):
	perm = np.random.permutation(train.shape[0])
	train = train[perm, :]
	label = label[perm]
	return train, label

train_data, train_labels = randomise(train_data, train_labels)
test_data, test_labels = randomise(test_data, test_labels)

#-----------------Logistic Regression--------------
'''
logistic_model = LogisticRegression(random_state=1, max_iter=100, solver='sag')
logistic_model.fit(train_data, train_labels)
correct_count = 0
for i in range(test_data.shape[0]):
	if logistic_model.predict(test_data[i]) == test_labels[i]:
		correct_count += 1

print('Accuracy % : ', correct_count * 100/test_data.shape[0])
input()
'''
#---------------Neural Network---------
nn_model = MLPClassifier(random_state = 1, hidden_layer_sizes = (3000, 1000, 100, 10), solver = 'lbfgs', activation = 'logistic', alpha=0.00001)
nn_model.fit(train_data, train_labels)
correct_count = 0
for i in range(test_data.shape[0]):
	if nn_model.predict(test_data[i]) == test_labels[i]:
		correct_count += 1

print('Accuracy % : ', correct_count * 100/test_data.shape[0])
input()
