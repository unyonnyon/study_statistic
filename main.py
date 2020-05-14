# %%

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%

# set params
params = {
    "loc": 150,
    "scale": 15,
    "size": 10000
}

# generate random values
height = np.random.normal(**params)
height_se = pd.Series(height)

# %%
plt.interactive(False)
plt.plot(height)
plt.show()

# %%

print("hello")
