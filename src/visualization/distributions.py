"""
Dataset distribution plots.
"""

import matplotlib.pyplot as plt


def target_distribution(values):

    plt.hist(values, bins=40)

    plt.xlabel("Target")

    plt.ylabel("Count")

    plt.show()


def feature_distribution(values):

    plt.hist(values, bins=40)

    plt.xlabel("Feature")

    plt.ylabel("Count")

    plt.show()
