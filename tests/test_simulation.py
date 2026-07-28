"""
Simulation tests.
"""

import numpy as np


def rc_voltage(t, tau):

    return 1 - np.exp(-t / tau)


def test_initial_voltage():

    assert rc_voltage(0, 1) == 0


def test_final_voltage():

    assert rc_voltage(100, 1) > 0.999
