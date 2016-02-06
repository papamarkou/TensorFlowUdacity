### Load packages

import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle

### Define environment variables

BASEDIR = "/Users/theodore/workspace/pycharm/TensorFlowUdacity"

DATADIR = os.path.join(BASEDIR, "data")
TRAINDATADIR = os.path.join(DATADIR, "notmnist", "notmnist_large")
TESTDATADIR = os.path.join(DATADIR, "notmnist", "notmnist_small")

### Define functions for getting array of directory paths and array of file paths

def get_dir_paths(root):
  return [os.path.join(root, n) for n in sorted(os.listdir(root)) if os.path.isdir(os.path.join(root, n))]

def get_file_paths(root):
  return [os.path.join(root, n) for n in sorted(os.listdir(root)) if os.path.isfile(os.path.join(root, n))]

### Get directory and file paths of training and test sets

train_data_paths = get_dir_paths(TRAINDATADIR)
test_data_paths = get_dir_paths(TESTDATADIR)

### Problem 1

## Display a sample of 5 images in their initial png format

nsamples = 5

for i in np.arange(nsamples):
    display(Image(filename=np.random.choice(get_file_paths(np.random.choice(test_data_paths)))))

## Set image properties

image_size = 28 # Pixel width and height
pixel_depth = 255.0  # Number of levels per pixel

## Read a sample image

image_file = np.random.choice(get_file_paths(np.random.choice(test_data_paths)))
image_data = ndimage.imread(image_file).astype(float)

## Show numeric representation of image

image_data

## Show type of image object

type(image_data)

## Show dimensions of image object

image_data.shape

## Plot image using imshow

plt.imshow(image_data)
plt.show()

## Plot image using a scatterplot

colors = [str(i/pixel_depth) for i in np.ravel(image_data)]
plt.scatter(
    np.tile(np.arange(image_size), image_size),
    np.repeat(np.flipud(np.arange(image_size)), image_size),
    s=150,
    c=colors,
    marker='s'
)
plt.show()

## Plot image using a scatterplot by setting cmap option

colors = [str(i/pixel_depth) for i in np.ravel(image_data)]
plt.scatter(
    np.tile(np.arange(image_size), image_size),
    np.repeat(np.flipud(np.arange(image_size)), image_size),
    s=150,
    c=colors,
    marker='s',
    cmap=plt.cm.viridis    
)
plt.show()

