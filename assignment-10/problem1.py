
# coding: utf-8

# In[1]:
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline
#plt.style.use('ggplot')


# In[2]:
fileIn = sys.argv[1]
# fileIn = "data/311_Service_Requests_from_2010_to_Present_2014.csv"
with open(fileIn, 'r') as f:
    df = pd.read_csv(f,
                     index_col = [u'Borough', u'Created Date'],
                     usecols = [u'Unique Key', u'Created Date', u'Borough'],
                     parse_dates = [u'Created Date'])


# In[3]:

#boroughs = list(df.index.levels[0])
boroughs = ['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']

dfCounts = pd.DataFrame(index = df.index.levels[1])
for borough in boroughs:
    dfCounts[borough] = df[u'Unique Key'][borough].resample('D', how = 'count')
dfCounts = dfCounts[pd.notnull(dfCounts.BRONX)]


# In[7]:

p1 = dfCounts.plot(figsize = (10, 6), lw = 1.4)
plt.show()


# In[ ]:



