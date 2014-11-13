
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import csv
from datetime import datetime

### settings (ipython notebook)
#get_ipython().magic(u'matplotlib inline')


# In[2]:

data_file = sys.argv[1]


# In[3]:

with open(data_file, 'r') as f:
    submissions = pd.read_csv(f, parse_dates=['timestamp'])


# In[4]:

grouped = submissions.groupby(submissions['timestamp'])
subs = grouped.count()
subs = subs.resample('4H', how = 'sum')


# In[6]:

width = 1.0/6

fig, ax = plt.subplots(figsize = (16, 6))
firstSub = subs.index[0]
lastSub = subs.index[-1]
color = "#BA5D25"
ax.bar(subs.index, height = subs.timestamp, width = width, lw = 0, color = color)

### annotations
fig.suptitle("Fall 2007 assignment submissions", fontsize = 14)
ax.set_ylabel("Number of submissions")
### ticks
xticks = ["2007-09-18 12:00:00", "2007-10-04 12:00:00",
         "2007-10-25 12:00:00", "2007-11-27 12:00:00",
         "2007-12-15 12:00:00", "2007-12-11 12:00:00"]
xtickAssignNum = [x for x in range(1, len(xticks) + 1)]
xticklabels = [xticks[i][5:11] + xticks[i][11:19] + "\n" + "Assign #" + str(xtickAssignNum[i]) for i in range(len(xticks))]
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels, rotation = 90, horizontalalignment='right')
ax.grid()
fig.subplots_adjust(bottom=.25)
plt.show()


# In[5]:



