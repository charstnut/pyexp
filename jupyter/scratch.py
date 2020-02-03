# %%
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Qt5Agg")

# %%
print("Hello, this is a test!")

# %%
x = np.arange(100)
y = x + np.random.rand(len(x)) * 1

plt.figure()
plt.plot(x, y)
plt.show()
# plt.close()

# %%

# %%
