
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


####### Proble 1c

# In[19]:

fig, [ax1, ax2] = plt.subplots(figsize = (10, 5),ncols = 2)

### plot 1
ax1.plot(stocks.apple, marker = "o", markersize = 5, color = "darkcyan", mec = "darkcyan", label = "Apple")

### plot 2
ax2.plot(stocks.microsoft, marker = "s", markersize = 5, color = "darkorange", mec = "darkorange", label = "Microsoft")

### axes labels and plot titles
fig.suptitle("Monthly stock prices", fontsize = 14)
ax1.set_ylabel("Price (USD)")
ax1.set_title("Apple")
ax2.set_title("Microsoft")
ax2.set_ylabel("Price (USD)")

### ticks and grids
xticks = [int(tick) for tick in ax1.get_xticks()]
xticks = [x * 3 for x in range(int(stocks.shape[0]/3))]
ax1.set_xticks(xticks)
ax2.set_xticks(xticks)
xticklabels = list(stocks.month[xticks])
ax1.set_xticklabels(xticklabels, rotation = 45, fontsize = 9)
ax2.set_xticklabels(xticklabels, rotation = 45, fontsize = 9)
ax1.grid()
ax2.grid()


### ylims
#y1lims = ax1.get_ylim()
#y2lims = ax2.get_ylim()
#ymax = max(y1lims[1], y2lims[1])
#ax1.set_ylim(0, ymax + 1.0/20 * ymax)
#ax2.set_ylim(0, ymax + 1.0/20 * ymax)
# xticks = [int(tick) for tick in ax1.get_xticks()]
# xticks = [x * 3 for x in range(int(stocks.shape[0]/3))]
# ax1.set_xticks(xticks)
# xticklabels = list(stocks.month[xticks])
# ax1.set_xticklabels(xticklabels, rotation = 45, fontsize = 9)
plt.show()


# In[ ]:



