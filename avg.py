import numpy as np


def mean_meas(measurements, precision):
    '''
	Calculate mean and combined error of several measurements with equal precision
	(e.g. Taking the same measurement several times)

	inputs:
	measurements, precision

	returns:
	mean, ce
	'''
    mean = np.mean(measurements)
    std = np.std(measurements, ddof=1)
    ce = np.sqrt(std**2 / len(measurements) + precision**2)

    return mean, ce


def wt_avg(data, error, precision):
    '''
	Calculate combined means with different uncertainties (error is std)

	inputs:
	data, error, precision

	returns:
	data_bar, error_bar
	'''
    weight = 1 / (error**2)
    data_bar = sum(weight * data) / sum(weight)
    se = 1 / np.sqrt(sum(weight))
    error_bar = np.sqrt(se**2 + precision**2)

    return data_bar, error_bar