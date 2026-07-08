"""
Reliability metrics.
"""

import numpy as np


def failure_rate(failures, total):
    return failures / total


def success_rate(successes, total):
    return successes / total


def availability(uptime, downtime):
    return uptime / (uptime + downtime)


def consistency(values):
    return 1.0 / (1.0 + np.var(values))
