# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
import pylab
import pandas as pd
from datetime import datetime
import sys
import matplotlib.cm as cm

### read data
in_file = "311_Service_Requests_from_2010_to_Present.csv"
with open(in_file, 'r') as f:
    df = pd.read_csv(f)

### grouping
grouped = df['Agency'].groupby(df['Agency'])
pr1_1 = grouped.count()

### Problem 1
pr1_agencies = ['NYPD','DOT','DOB','TLC','DPR']

fig, ax1 = plt.subplots()
centers = range(len(pr1_agencies))
for i in range(len(pr1_agencies)):
  plt.bar(centers[i], pr1_1[pr1_agencies][i])
ax1.set_title('Complaint volumes by agency')
ax1.set_xlabel('Agency')
ax1.set_ylabel('Volume')
xlim = ax1.get_xlim()
xlim = (xlim[0]-0.25, xlim[1])
ax1.set_xlim(xlim)
ax1.set_xticks([x+0.75/2 for x in centers])
ax1.set_xticklabels(pr1_agencies)
plt.show()
