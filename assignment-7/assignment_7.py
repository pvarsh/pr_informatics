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
