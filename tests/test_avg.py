import pytest

import sys
sys.path.append('..')

import pyexp
from pyexp import avg

import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp


def test_avg():
    meas = np.arange(1, 7)
    average = avg.weighted_avg(meas)
    assert unp.nominal_values(average) == 3.5
    assert unp.std_devs(average) == np.std(meas, ddof=1) / np.sqrt(len(meas))
