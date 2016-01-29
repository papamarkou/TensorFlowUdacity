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

DATADIR = "data"

os.path.join(BASEDIR, DATADIR)

num_classes = 10

def get_data_folders(root):
  data_folders = [os.path.join(root, d) for d in sorted(os.listdir(root)) if d != '.DS_Store']
  if len(data_folders) != num_classes:
    raise Exception(
      'Expected %d folders, one per class. Found %d instead.' % (
        num_classes, len(data_folders)))
  print(data_folders)
  return data_folders

train_folders = extract(train_filename)
test_folders = extract(test_filename)

