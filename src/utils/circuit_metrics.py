"""
Electrical engineering metrics.
"""

import numpy as np


def relative_error(
        true,
        predicted):

    return np.mean(
        np.abs(
            (true - predicted) / true
        )
    )


def mse(
        true,
        predicted):

    return np.mean(
        (true - predicted) ** 2
    )


def maximum_error(
        true,
        predicted):

    return np.max(
        np.abs(
            true - predicted
        )
    )


def mean_percentage_error(
        true,
        predicted):

    return np.mean(
        np.abs(
            (true - predicted)
            / true
        )
    ) * 100
