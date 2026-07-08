"""
Learning curve visualization.
"""

import matplotlib.pyplot as plt


def learning_curve(train, validation):

    plt.plot(train)

    plt.plot(validation)

    plt.xlabel("Training Samples")

    plt.ylabel("Score")

    plt.legend(["Training", "Validation"])

    plt.show()
