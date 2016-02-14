A Companion to TensorFlow Udacity MOOC (WIP)
==========================================================================================

This repository aims at accompanying and complementing the Python code of the
[TensorFlow Udacity MOOC by Google](https://www.udacity.com/course/viewer#!/c-ud730). It provides one possible solution to
the MOOC quizzes and assignments. When deemed useful, alternative solutions or elaborations are provided to clarify
concepts or methods.

Jupyter notebooks are used for formatting the code in order to display textual and visual output along with code. The
notebooks have been developed using Python 2.7.11 (work in progress). If you would like to recommend any improvements, feel
free to open a PR or issue.

Before getting started, two steps need to be taken:

1. Every notebook sets `BASEDIR`. You need to set `BASEDIR` to the root of your cloned git repository. In the future, this
  git repository might be turned to a Python package to avoid manual configuration of paths.
2. For assignment 1, download the [notMNIST data](http://yaroslavvb.blogspot.co.uk/2011/09/notmnist-dataset.htmlS).
  More specifically, download the [large notMNIST](http://yaroslavvb.com/upload/notMNIST/notMNIST_large.tar.gz) and
  [small notMNIST](notMNIST_small.tar.gz) datasets, decompress them and place them in
  `BASEDIR/data/notmnist/notmnist_large` and `BASEDIR/data/notmnist/notmnist_small` respectively. The large and small
  notMNIST datasets correspond to the training and test set. For instance, the training data for letter A should be located
  in `BASEDIR/data/notmnist/notmnist_large/A` after downloading, decompressing and moving the training data.
