
# coding: utf-8

# In[2]:

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc
import sys

#%matplotlib inline


# In[4]:

if len(sys.argv) == 2:
    datafile = sys.argv[1]
else:
    datafile = "microprocessors.dat"
    
with open(datafile, 'r') as f:
    procs = pd.read_csv(datafile)


# In[45]:

procs['log_trans'] = np.log10(procs['Transistors'])
procs.sort(columns = 'log_trans', inplace = True)
procs.index = range(len(procs))
procs


# In[51]:

fig, axs = plt.subplots(ncols = 2, figsize = (10, 6), sharey = True)
nrows = procs.shape[0]

axs[0].plot(procs['Year of Introduction'], range(nrows), 'or')
axs[1].plot(procs['log_trans'], range(nrows), 'or')

xticks = [int(tick) for tick in axs[1].get_xticks()]
xticks = [r'$10^{%d}$' %tick for tick in xticks]
axs[1].set_xticklabels(xticks, fontsize = 12)

axs[0].set_yticks(range(nrows))
axs[0].set_yticklabels(procs.Processor)

axs[0].set_ylim((-1, nrows + 0.5))

axs[0].set_title('Year of introduction')
axs[1].set_title('Number of transistors')
fig.suptitle('Microprocessors', fontsize = 16)

for i in range(2):
    axs[i].grid(axis = 'y')

fig.subplots_adjust(left=.25)

plt.show()

