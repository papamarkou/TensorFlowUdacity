"""Softmax"""

# Load packages

import matplotlib.pyplot as plt
import numpy as np

# Define softmax function

def softmax(x):
    """Compute softmax values for each sets of scores in x"""
    result = np.empty(x.shape)

    for i in np.arange(0, scores.shape[1]):
        expscores = np.exp(scores[:, i])
        result[:, i] = expscores/np.sum(expscores)

    return result

# Generate a set of scores

x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
softmaxvalues = softmax(scores)

# Plot softmax curves

colors = ('red', 'green', 'blue')

for i in np.arange(0, softmaxvalues.shape[0]):
    plt.plot(x, softmaxvalues[i, :], color=colors[i], linewidth=2)

plt.show()
