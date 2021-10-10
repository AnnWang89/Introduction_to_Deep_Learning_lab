# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:18:03 2021

@author: 安ㄢ
"""


from glob import glob
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras import optimizers, regularizers, metrics, regularizers, models, layers, utils
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import ntpath
from keras.applications import VGG16
from PIL import Image 
from random import shuffle
from sklearn.preprocessing import OneHotEncoder
import os

trainCSV=pd.read_csv("test.csv")

test_path = 'test_images/'

all_testing_files = glob("test_images/*.jpg")
print(len(all_testing_files))

# ??????
shuffles = np.random.permutation(all_testing_files)

if len(all_testing_files) > 0:
    for i in range(0, len(all_testing_files)):
        file=ntpath.basename(shuffles[i])
        label=trainCSV.loc[trainCSV['ID'] == file, 'Label'].iloc[0]
        newpath=shuffles[i].replace('test_images', test_path+str(label))
        os.rename(shuffles[i], newpath)