import warnings
import numpy as np
import scipy as sp
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy import optimize, stats, integrate

# TODO: Change this into a class-based method


def fit(model,
        pars_list,
        x_data,
        y_data,
        y_err=None,
        x_fit_samples=1000,
        print_pars=True):
    # Simple fit utility, prints output and returns popt as uncertainties array along with simulation and normalized residuals

    if y_err is None:
        y_err = np.ones(y_data)

    # Perform fitting
    par0 = np.ones(len(pars_list))  # initial guesses
    popt, pcov = sp.optimize.curve_fit(model,
                                       x_data,
                                       y_data,
                                       p0=par0,
                                       sigma=y_err,
                                       absolute_sigma=True)
    # print('parameter covariance matrix: \n', pcov)
    perr = np.sqrt(np.diag(pcov))
    pars_opt = unp.uarray(popt, perr)

    if print_pars:
        for i, p in enumerate(pars_list):
            print('{} = {:.1u}'.format(p, pars_opt[i]))

    x_fit = np.linspace(x_data.min(), x_data.max(), x_fit_samples)
    y_fit = model(x_fit, *popt)

    resid = (y_data - y_fit) / y_err

    return pars_opt, x_fit, y_fit, resid


def chi_sq(x_data, y_data, y_err, model, popt):
    # Calculate chi_sq according to fit results
    difference = y_data - model(x_data, *popt)

    chi_2 = np.sum((difference / y_err)**2)
    dof = len(difference) - len(popt)

    p_val = 1 - sp.stats.chi2.cdf(chi_2, df=dof)

    return chi_2, p_val


def chi_sq_hypotest(bins, counts, model, popt):
    # Perform a chi-squared test on binned distributions, and returns
    # by default.
    # Note: model should output counts (norm * total counts) so that it can be directly integrated. Has to be continuous!
    # Note: counts should be greater than 5!
    if np.any(counts < 5):
        warnings.warn("Some counts are smaller than 5, consider rebinning!")
    assert len(bins) == len(counts) - 1

    expected_cnts = []
    f = lambda x: model(x, *popt)

    expected_cnts.append(sp.integrate.quad(f, -np.inf, bins[0]))
    for i in range(bins):
        expected_cnts.append(sp.integrate.quad(f, bins[i], bins[i + 1]))
    expected_cnts.append(sp.integrate.quad(f, bins[-1], np.inf))
    expected_cnts = np.asarray_chkfinite(expected_cnts)

    dof = len(counts) - len(popt)

    return sp.stats.chisquare(counts, expected_cnts, ddof=dof)
