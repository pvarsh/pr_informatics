
# coding: utf-8

# In[4]:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

### settings (ipython notebook)
#%matplotlib inline


# In[5]:

data_file = sys.argv[1]
#data_file = "stocks.dat"


# In[6]:

with open(data_file, 'r') as f:
    stocks = pd.read_csv(f)
stocks.sort(columns = ['month'], inplace = True)
stocks.index = range(stocks.shape[0])


####### Problem 1a

# In[9]:

fig, ax = plt.subplots(figsize = (10, 6))
ax.plot(stocks.apple, marker = "o", markersize = 5, color = "darkcyan", mec = "darkcyan", label = "Apple")


## axes labels and titles
ax.set_title("Monthly Apple stock prices")
ax.set_ylabel("Stock price ($)")

### ticks and grid
xticks = [int(tick) for tick in ax.get_xticks()]
xticks = [x * 3 for x in range(int(stocks.shape[0]/3))]
ax.set_xticks(xticks)
xticklabels = list(stocks.month[xticks])
ax.set_xticklabels(xticklabels, rotation = 45, fontsize = 9)
ax.grid()

### axes lims
ylims = ax.get_ylim()
ax.set_ylim((ylims[0], ylims[1] + 10))

plt.show()

