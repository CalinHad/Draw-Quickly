from keras.models import load_model
from keras.utils import np_utils
from random import randint
import numpy as np
import os
from PIL import Image
from matplotlib.image import imread
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#files = ["Image1.tiff", "Image2.tiff", "Image3.tiff", "Image4.tiff","Image5.tiff"]
#model = load_model('images.h5')

"""
basewidth = 28
img = Image.open('Image1.tiff')

hsize =28
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('tran1.jpg')

"""



img = imread('tran1.jpg')
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('tran1.jpg')
img = rgb2gray(img)


files=[img]


def load(f):
    data = []
    for file in files:
        new_f = []
        for i in range(len(f)):
            x = np.reshape(f[i], (28, 28))
            x = np.expand_dims(x, axis=0)
            x = np.reshape(f[i], (28, 28, 1))
            new_f.append(x)
        f = new_f
        data.append(f)
    return data

def normalize(data):
    return np.interp(data, [0, 255], [-1, 1])


Imgs = load(files)
Imgs = list(map(normalize, Imgs))
print(Imgs)