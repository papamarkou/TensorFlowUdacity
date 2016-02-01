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

BASEDIR = "/Users/theodore/workspace/pycharm/TensorFlowUdacity"

DATADIR = os.path.join(BASEDIR, "data")
TRAINDATADIR = os.path.join(DATADIR, "notmnist", "notmnist_large")
TESTDATADIR = os.path.join(DATADIR, "notmnist", "notmnist_small")

def get_dir_paths(root):
  return [os.path.join(root, n) for n in sorted(os.listdir(root)) if os.path.isdir(os.path.join(root, n))]

def get_file_paths(root):
  return [os.path.join(root, n) for n in sorted(os.listdir(root)) if os.path.isfile(os.path.join(root, n))]

train_data_paths = get_dir_paths(TRAINDATADIR)
test_data_paths = get_dir_paths(TESTDATADIR)

nsamples = 5

for i in np.arange(nsamples):
    display(Image(filename=np.random.choice(get_file_paths(np.random.choice(test_data_paths)))))
