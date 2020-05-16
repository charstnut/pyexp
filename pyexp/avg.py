import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp


def weighted_avg(meas, error=None, prec=None, axis=None):
    """Returns the weighted average of the measurement. There are two cases: 
	When calculating human read measurements, the standard deviation plus device precision are independent sources of error.
	When assuming errors are truly gaussian, apply the stantard weighted average.
	
	Arguments:
		meas {np array} -- Input measurements
	
	Keyword Arguments:
		error {np array} -- gaussian error (default: {None})
		prec {double} -- device precision (e.g. 0.1 cm) (default: {None})
	
	Returns:
		uncertainty array -- average and combined error
	"""

    # Init prec to 0 if None
    if prec is None:
        prec = 0

    # Stat error (random error)
    std = np.std(meas, ddof=1, axis=axis)

    if axis is None:
        N = len(meas.flatten())
    else:
        N = meas.shape[axis]

    if error is None:
        # As in case of calculating human-read meas
        mean = np.average(meas, axis=axis)
        combined_error = np.sqrt(std**2 / N + prec**2)
    else:
        # Assuming errors are truly gaussian
        w = 1. / error**2
        mean = np.average(meas, weights=w, axis=axis)
        combined_error = np.sqrt(1. / np.sum(w, axis=axis))

    average = unp.uarray(mean, combined_error)

    return average
