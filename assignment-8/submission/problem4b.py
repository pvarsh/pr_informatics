
# coding: utf-8

# In[1]:

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import sys

#%matplotlib inline


# In[2]:

#datafile = "genes.dat"
if len(sys.argv) == 2:
    datafile = sys.argv[1]
with open(datafile, 'r') as f:
    genes = pd.read_csv(datafile)


# In[3]:

fig, axs = plt.subplots(nrows = 4, ncols = 4, figsize = (9, 9))

cPoint = "#52B8E0"
cLine = "#D19047"

for i, row in enumerate(genes.columns):
    for j, col in enumerate(genes.columns):
        axs[j][i].scatter(genes[row], genes[col], c = cPoint)
        if j != 3:
            axs[j][i].set_xticklabels('')
        if i != 0:
            axs[j][i].set_yticklabels('')
        if j == 0:
            axs[j][i].xaxis.set_label_position('top')
            axs[j][i].set_xlabel(row)
        if i == 3:
            axs[j][i].yaxis.set_label_position('right')
            axs[j][i].set_ylabel(col, rotation = 'horizontal')#, bbox = [1,1])

poly_C = np.poly1d(np.polyfit(genes.C, genes.A, 1))
xC = np.linspace(-.1, 1.1)
axs[0][2].plot(xC, poly_C(xC), '-', lw = 3, c = cLine)            
            
poly_D = np.poly1d(np.polyfit(genes.D, genes.A, 3))
xD = np.linspace(-.1, 1.1)
axs[0][3].plot(xD, poly_D(xD), '-', lw = 3, c = cLine)

poly_B = np.poly1d(np.polyfit(genes.B, genes.A, 5))
xB = np.linspace(-.1, 1.1)
axs[0][1].plot(xB, poly_B(xB), '-', lw = 3, c = cLine)

for ind, val in np.ndenumerate(axs):
    axs[ind].set_xlim((-.1, 1.1))
    axs[ind].set_ylim((-.1, 1.1))

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.1, hspace=.1)
plt.show()


# In[4]:

# pd.scatter_matrix(genes, alpha=0.2, figsize=(8, 8), diagonal='kde');


# In[ ]:



