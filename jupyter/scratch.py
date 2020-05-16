# %%
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Qt5Agg")

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyexp.avg as avg

# import iminuit, probfit
import scipy.stats

# np.random.seed(1)
# data = np.random.exponential(0.5, 500)

# def unbinned_exp_LLH(data, loc_init, scale_init, limit_loc, limit_scale):
#     # Define function to fit
#     def exp_func(x, loc, scale):
#         return scipy.stats.expon.pdf(x, loc, scale)

#     # Define initial parameters
#     init_params = dict(loc=loc_init, scale=scale_init)

#     # Create an unbinned likelihood object with function and data.
#     unbin = probfit.UnbinnedLH(exp_func, data)

#     # Minimizes the unbinned likelihood for the given function
#     m = iminuit.Minuit(unbin,
#                        **init_params,
#                        limit_scale=limit_loc,
#                        limit_loc=limit_scale,
#                        pedantic=False,
#                        print_level=0)
#     m.migrad()
#     params = m.values.values()  # Get out fit values
#     errs = m.errors.values()
#     return params, errs

# params, errs = unbinned_exp_LLH(data,
#                                 loc_init=0,
#                                 scale_init=0.5,
#                                 limit_loc=(-1, 1),
#                                 limit_scale=(-1, 1))

# loc, scale = params

# # Plot
# x_pts = np.linspace(0, 3, 100)
# plt.plot(x_pts,
#          scipy.stats.expon.pdf(x_pts, *params),
#          label="exp(-{1:.2f}x)".format(*params),
#          color="black")
# plt.hist(data, color="lightgrey", bins=20, label="generated data", normed=True)
# plt.xlim(0, 3)
# plt.legend()
# plt.show()
