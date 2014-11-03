
# coding: utf-8

# In[1]:

import numpy as np
from matplotlib import pyplot as plt
import pylab
import pandas as pd
from datetime import datetime
import sys
import matplotlib.cm as cm
import re

### settings
#get_ipython().magic(u'matplotlib inline')

####### Command line parameters

in_file, k = sys.argv[1:3]
k = int(k)

####### Functions

# In[2]:

def top_k_types(df, k):
    """ returns a series of top k complaint types """
    grouped = df['Complaint Type'].groupby(df['Complaint Type'])
    complaints = grouped.count().sort(inplace = False, ascending = False)
    return complaints[0:k]

def top_k_agencies(df, k):
    """ returns a series of top k agencies by number of complaints """
    grouped = df['Agency'].groupby(df['Agency'])
    complaints = grouped.count().sort(inplace = False, ascending = False)
    return list(complaints.keys())[0:k]

def get_first_monday(dates):
    """ returns the index of the first monday in a list of dates """
    return 7%dates[0].weekday()

def complaint_tseries_agency(df, agencies):
    """ plots something """
    dates = list( ag_date_counts.keys().levels[1] )
    first_monday = get_first_monday(dates)
    num_weeks = len(dates)/7
    #print num_weeks
    xticks = [first_monday + 7 * x for x in range(num_weeks)]
    fig, ax = subplots(figsize = (10, 5))
    #print type(ag_date_counts.keys())
    colors = list(np.linspace(0, 1, len(agencies) + 2))[1:-1]
    #print colors
    for i, agency in enumerate(agencies):
        ax.plot(ag_date_counts[agency], c = cm.Set1(colors[i]), label = agency)
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of complaints")
    ax.grid(b=True, which='major', axis = 'x', color='gray', linestyle='--')
    ax.legend(loc = 'best')
    ax.set_xticks(xticks)
    ticklabels = [datetime.strftime(dates[xtick], "%m/%d") for xtick in xticks]
    ax.set_xticklabels(ticklabels)
    daterange = (datetime.strftime(dates[0], "%m/%d/%Y"), datetime.strftime(dates[-1], "%m/%d/%Y"))
    ax.set_title("Complaint volumes by agency %s - %s" %daterange)
    plt.show()


# In[3]:

### read data
### reading is slow due to parsing two columns as datetime
#in_file = "311_Service_Requests_from_2010_to_Present.csv"
with open(in_file, 'r') as f:
    df = pd.read_csv(f,
                     index_col = ['Unique Key'],
                     dtype = {'Incident Zip': str})
                     #parse_dates=['Created Date','Closed Date'])


####### Min and max dates

# In[4]:

### Use this block if dates are parsed in data frame
# datemin = min(df['Created Date'])
# datemax = max(df['Created Date'])
# datemin_str = datetime.strftime(datemin, "%b/%d/%Y")
# datemax_str = datetime.strftime(datemax, "%b/%d/%Y")
datemin_str = "Jun/01/2013"
datemax_str = "Aug/31/2013"


####### Grouping

# In[5]:

#grouped = df['Agency'].groupby(df['Agency'])
#pr1_1 = grouped.count()


####### Problem 2

# In[7]:

complaint_types = top_k_types(df, k)
#print list(complaint_types.keys())
fig, ax = plt.subplots(figsize = (10, 5))
xpos = [1*x for x in range(len(complaint_types))]
plt.bar(xpos, complaint_types, align = 'center', width = .8, color = cm.Blues(0.4), zorder = 3)
ax.set_title("Top %d complaint types %s-%s" %(k, datemin_str, datemax_str))
ax.set_xticks(xpos)
lbls = list(complaint_types.keys())
ax.set_xticklabels(complaint_types.keys(), fontsize = 7)
ax.set_xlabel("Complaint Type")
ax.set_ylabel("Volume")
ax.grid(b=True, which='major', axis = 'y', color='gray', linestyle='--', alpha = 0.4, zorder = 0)
ax.set_xlim(-.75, len(complaint_types)-.25)
plt.show()


# In[ ]:



