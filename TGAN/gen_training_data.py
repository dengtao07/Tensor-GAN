# -*- coding:utf-8 -*-
# 
# Author: YIN MIAO
# Time: 2018/10/22 17:24

import tensorflow as tf
import numpy as np
import sys
import scipy.io as sio
import os
import keras
from skimage import transform
from matplotlib import pyplot as plt


if __name__ == '__main__':
    n_slice = 7
    n_step = 1
    img_shape = (28, 28, 1)

    (x_train, y_train), (_, _) = keras.datasets.mnist.load_data()
    x_train = x_train / 255.
    n_sample = len(x_train)
    datas = np.zeros((n_sample, img_shape[0], img_shape[1], n_slice))
    for i in range(n_sample):
        for k in range(n_slice):
            data = x_train[i]
            datas[i, :, 0:(img_shape[0] - n_slice + n_step * k), k] = data[:, (n_slice - n_step * k):img_shape[1]]

    sio.savemat('./data/mnist_28_28_7.mat', {'XX':datas})