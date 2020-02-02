import pytest
import avg

import numpy as np
import uncertainties as unc


def test_avg():
    meas = np.arange(1, 7)
    average = avg.weighted_avg(meas)
    assert average.n == 3.5
    assert average.s == np.std(meas, ddof=1) / np.sqrt(len(meas))