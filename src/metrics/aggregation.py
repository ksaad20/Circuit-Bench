"""
Metric aggregation utilities.
"""

import numpy as np


def arithmetic_mean(values):
    return float(np.mean(values))


def geometric_mean(values):
    values = np.asarray(values, dtype=float)
    values = values[values > 0]
    return float(np.exp(np.mean(np.log(values))))


def harmonic_mean(values):
    values = np.asarray(values, dtype=float)
    return float(len(values) / np.sum(1.0 / values))


def weighted_average(values, weights):
    return float(np.average(values, weights=weights))


def aggregate_metrics(metrics: dict):
    return {
        "mean": arithmetic_mean(list(metrics.values())),
        "geometric_mean": geometric_mean(list(metrics.values())),
        "harmonic_mean": harmonic_mean(list(metrics.values()))
    }
