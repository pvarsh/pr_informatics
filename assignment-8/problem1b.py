
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

### settings (ipython notebook)
#%matplotlib inline


# In[2]:

data_file = sys.argv[1]
#data_file = "stocks.dat"


# In[3]:

with open(data_file, 'r') as f:
    stocks = pd.read_csv(f)
stocks.sort(columns = ['month'], inplace = True)
stocks.index = range(stocks.shape[0])


####### Problem 1b

# In[5]:

fig, ax = plt.subplots(figsize = (10,6))
ax.plot(stocks.apple, marker = "o", markersize = 5, color = "darkcyan", mec = "darkcyan", label = "Apple")
ax.plot(stocks.microsoft, marker = "s", markersize = 5, color = "darkorange", mec = "darkorange", label = "Microsoft")
xticks = [int(tick) for tick in ax.get_xticks()]
xticks = [x * 3 for x in range(int(stocks.shape[0]/3))]
ax.set_xticks(xticks)
xticklabels = list(stocks.month[xticks])
ylims = ax.get_ylim()
ax.set_ylim(0, ylims[1] + 1.0/10 * ylims[1])
ax.grid()
### annotations
ax.set_title("Monthly Apple and Microsoft stock prices")
ax.set_ylabel("Price")
ax.legend(loc = 2)
#print stocks.month[xticks]
ax.set_xticklabels(xticklabels, rotation = 45, fontsize = 9)
plt.show()

