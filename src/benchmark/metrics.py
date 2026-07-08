"""
Performance metrics for CircuitBench.
"""

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

import numpy as np


def mae(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)


def mse(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)


def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


def r2(y_true, y_pred):
    return r2_score(y_true, y_pred)


def mape(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return np.mean(np.abs((y_true-y_pred)/y_true))*100


def max_error(y_true,y_pred):
    return np.max(np.abs(np.asarray(y_true)-np.asarray(y_pred)))
