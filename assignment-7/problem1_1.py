
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

####### Getting parameters

in_file = sys.argv[1]

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
    print num_weeks
    xticks = [first_monday + 7 * x for x in range(num_weeks)]
    fig, ax = subplots(figsize = (10, 5))
    print type(ag_date_counts.keys())
    colors = list(np.linspace(0, 1, len(agencies) + 2))[1:-1]
    print colors
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

# ### Use this block if dates are parsed in data frame
# datemin = min(df['Created Date'])
# datemax = max(df['Created Date'])
# datemin_str = datetime.strftime(datemin, "%b/%d/%Y")
# datemax_str = datetime.strftime(datemax, "%b/%d/%Y")
datemin_str = "Jun/01/2013"
datemax_str = "Aug/31/2013"


####### Grouping

# In[5]:

grouped = df['Agency'].groupby(df['Agency'])
pr1_1 = grouped.count()


# In[6]:

### Problem 1
pr1_agencies = ['NYPD','DOT','DOB','TLC','DPR']


# In[7]:

fig, ax = plt.subplots(figsize = (10, 5))
xpos = range(len(pr1_agencies))
plt.bar(xpos, pr1_1[pr1_agencies], align = 'center', color = cm.Blues(0.4), zorder = 3)
ax.set_xticks(xpos)
ax.set_xlabel("Agency")
yticks = [int(x) for x in ax.get_yticks()]
ax.set_yticklabels(yticks, fontsize = 8)
ax.set_ylabel("Volume")
ax.set_title("Complaint volumes by agency between %s - %s" %(datemin_str, datemax_str), fontsize = 9)
ax.set_xticklabels( pr1_agencies, fontsize = 9)
ax.grid(b=True, which='major', axis = 'y', color='gray', linestyle='--', alpha = 0.4, zorder = 0)
xlims = ax.get_xlim()
ax.set_xlim(-.75, len(pr1_agencies)-.25)
plt.show()

