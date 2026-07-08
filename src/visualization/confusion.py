"""
Confusion matrix plotting.
"""

import matplotlib.pyplot as plt


def plot_confusion(matrix):

    plt.imshow(matrix)

    plt.xlabel("Predicted")

    plt.ylabel("Actual")

    plt.colorbar()

    plt.show()
