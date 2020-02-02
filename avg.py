import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp


def weighted_avg(meas, error=None, prec=None):
    """Returns the weighted average of the measurement. There are two cases: 
	When calculating human read measurements, the standard deviation plus device precision are independent sources of error.
	When assuming errors are truly gaussian, apply the stantard weighted average.
	
	Arguments:
		meas {np array} -- Input measurements
	
	Keyword Arguments:
		error {np array} -- gaussian error (default: {None})
		prec {double} -- device precision (e.g. 0.1 cm) (default: {None})
	
	Returns:
		uncertainty ufloat -- average and combined error
	"""

    # Init prec to 0 if None
    if prec is None:
        prec = 0

    # Stat error (random error)
    std = np.std(meas, ddof=1)

    if error is None:
        mean = np.average(meas)  # As in case of calculating human-read meas
        combined_error = np.sqrt(std**2 / len(meas) + prec**2)
    else:
        # Assuming errors are truly gaussian
        w = 1. / error**2
        mean = np.average(meas, weights=w)
        combined_error = np.sqrt(1. / np.sum(w))

    average = unc.ufloat(mean, combined_error)

    return average
