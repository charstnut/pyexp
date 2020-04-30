import os
import sys
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

import avg

import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp


def test_avg():
    meas = np.arange(1, 7)
    print("Hello!")
    average = avg.weighted_avg(meas)
    assert unp.nominal_values(average) == 3.5
    assert unp.std_devs(average) == np.std(meas, ddof=1) / np.sqrt(len(meas))
