
# coding: utf-8

# In[30]:

import numpy as np
from matplotlib import pyplot as plt
import pylab
import pandas as pd
from datetime import datetime
import sys
import matplotlib.cm as cm
#import re
import csv

### settings (for ipython only)
#get_ipython().magic(u'matplotlib inline')

in_file = sys.argv[1]
zipcode_file = sys.argv[2]

####### Read 311 data

# In[3]:

### read data
### reading is slow due to parsing two columns as datetime
#in_file = "311_Service_Requests_from_2010_to_Present.csv"
with open(in_file, 'r') as f:
    df = pd.read_csv(f,
                     index_col = ['Unique Key'],
                     dtype = {'Incident Zip': str})
                     #parse_dates=['Created Date', 'Closed Date'])


####### Cleaning zip codes

# In[4]:

### filling NaN values in order to be able to run pd.str functions
df['Incident Zip'] = df['Incident Zip'].fillna(0).astype(str)
### delete '-' and everything after on ZIP+4 codes
df['Incident Zip'] = df['Incident Zip'].str.replace(r'-.*', '')
### drop rows with non-numeric characters in zip code
df['Incident Zip'].loc[df['Incident Zip'].str.contains(r'[\D]')] = '0'
### rows with zip codes over 5 digits long set to '0'
df['Incident Zip'].loc[df['Incident Zip'].apply(len) > 5] = '0'
### zero pad on the left
df['Incident Zip'] = df['Incident Zip'].apply(lambda x: x.zfill(5))


####### Read ZIP codes with populations data

# In[5]:

#zipcode_file = "zipCodePopulationData.csv"
with open(zipcode_file, 'r') as f:
    zipcodes = pd.read_csv(f)
zipcodes['Zip Code ZCTA'] = zipcodes['Zip Code ZCTA'].astype(str).apply(lambda x: x.zfill(5))


####### Group by zip code

# In[6]:

grouped_zip = df['Incident Zip'].groupby(df['Incident Zip'])
zip_counts = grouped_zip.count()[0:-2]
zip_counts = pd.DataFrame({'Incident Zip': zip_counts.keys(), 'Number of Complaints': zip_counts})
zip_counts = zip_counts[0:-2]
zip_counts['Incident Zip'] = zip_counts['Incident Zip'].astype(int).astype(str)
zip_counts['Incident Zip'] = zip_counts['Incident Zip'].apply(lambda x: x.zfill(5))


####### Merge

# In[7]:

zip_pop_count = pd.merge(zipcodes, zip_counts, left_on ='Zip Code ZCTA', right_on='Incident Zip')
zip_pop_count = zip_pop_count[['Incident Zip', '2010 Census Population', 'Number of Complaints']]
zip_pop_count.columns = ['zip', 'population', 'complaints']


####### Plot

# In[32]:

fig, ax = plt.subplots(figsize = (10, 5))
ax.scatter(zip_pop_count['population'], zip_pop_count['complaints'], lw = 0, c = '#a65200')
ax.set_xlabel('2010 census population')
ax.set_ylabel('Number of 311 complaints')
ax.set_title('311 Complaints by Zip Code Jun/1/2013-Aug/31/2013')
xlims = ax.get_xlim()
ax.set_xlim(xlims[0]/4, xlims[1])
ylims = ax.get_ylim()
ax.set_ylim(ylims[0]/2.5, ylims[1])
plt.show()


####### 0 or 1 complaints

# In[10]:

# ###Having only 0 or 1 complaints in a zip code is strange. This block looks at those zip codes.
# print "Zip codes with 1 complaint: %d" %zip_pop_count[zip_pop_count['complaints'] == 1].shape[0]
# print "Zip codes with 0 complaints: %d" %zip_pop_count[zip_pop_count['complaints'] == 0].shape[0]
# n = 1
# print "Zip codes with %d complaints:" %n
# zip_pop_count[zip_pop_count['complaints'] == n]


####### Read borough zips (downloaded from http://nyc.pediacities.com/New_York_City_ZIP_Codes)

# In[11]:

zipbor_f = "zip_borough.csv"
boroughs = sorted(['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'])
boroughs = {borough: i+1 for i, borough in enumerate(boroughs)}

### This block can be used if there's a file with zips and boroughs 
# with open(zipbor_f, 'rU') as f:
#     zipbor_d = {}
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         zipbor_d[row[0]] = boroughs[row[1]]


####### Hard coded zip to borough dictionary

# In[12]:

zipbor_d = {'10065': 3, '10069': 3, '10453': 1, '10013': 3, '10451': 1, '10457': 1, '10456': 1, '10455': 1, '10012': 3, '10459': 1, '11361': 4, '11232': 2, '10010': 3, '11385': 4, '10017': 3, '10016': 3, '11237': 2, '10454': 1, '10304': 5, '11218': 2, '10282': 3, '10280': 3, '10281': 3, '10115': 3, '10111': 3, '11109': 4, '11379': 4, '11378': 4, '10452': 1, '11102': 4, '11103': 4, '11377': 4, '11101': 4, '11106': 4, '11104': 4, '11105': 4, '11375': 4, '11374': 4, '10048': 3, '11229': 2, '10040': 3, '11371': 4, '11228': 2, '10044': 3, '11201': 2, '11203': 2, '10128': 3, '11205': 2, '11204': 2, '11207': 2, '11206': 2, '11209': 2, '11208': 2, '11372': 4, '11225': 2, '11224': 2, '11368': 4, '11369': 4, '11366': 4, '11223': 2, '11364': 4, '11365': 4, '11362': 4, '11363': 4, '11360': 4, '11222': 2, '11221': 2, '11220': 2, '11212': 2, '11213': 2, '11210': 2, '11211': 2, '10039': 3, '11217': 2, '11214': 2, '11215': 2, '10035': 3, '10034': 3, '10037': 3, '10036': 3, '10031': 3, '10030': 3, '10033': 3, '10032': 3, '11001': 4, '11358': 4, '11005': 4, '11004': 4, '11697': 4, '11694': 4, '11357': 4, '11356': 4, '11355': 4, '11354': 4, '11216': 2, '11451': 4, '10038': 3, '11096': 4, '10309': 5, '10308': 5, '10307': 5, '10306': 5, '10305': 5, '10461': 1, '10303': 5, '10302': 5, '10301': 5, '10028': 3, '10029': 3, '10026': 3, '10027': 3, '10024': 3, '10025': 3, '10022': 3, '10023': 3, '10020': 3, '10021': 3, '11219': 2, '11429': 4, '11428': 4, '11421': 4, '11420': 4, '11423': 4, '11422': 4, '11427': 4, '11426': 4, '10310': 5, '10312': 5, '10314': 5, '11359': 4, '11238': 2, '11239': 2, '10019': 3, '10018': 3, '11230': 2, '11231': 2, '10011': 3, '11233': 2, '11234': 2, '11235': 2, '11236': 2, '10014': 3, '11432': 4, '11433': 4, '11430': 4, '11436': 4, '11434': 4, '11435': 4, '10004': 3, '10005': 3, '10006': 3, '10007': 3, '10001': 3, '10002': 3, '10003': 3, '11692': 4, '10009': 3, '10475': 1, '10474': 1, '10471': 1, '10470': 1, '10473': 1, '10472': 1, '11691': 4, '11226': 2, '10075': 3, '10466': 1, '10467': 1, '10465': 1, '10462': 1, '10460': 1, '11040': 4, '10468': 1, '10469': 1, '11411': 4, '11412': 4, '11413': 4, '11414': 4, '11415': 4, '11416': 4, '11417': 4, '11418': 4, '11419': 4, '11251': 2, '10458': 1, '11367': 4, '11373': 4}


####### Plot with borough colors

# In[31]:

bors = []
for z in zip_pop_count['zip']:
    if z in zipbor_d:
        bors.append(zipbor_d[z])
    else:
        bors.append(6)
zip_pop_count['borough'] = bors
inv_bors = [1.0/bor for bor in bors]
fig, ax = plt.subplots(figsize=(10, 5))
colors = [k * 1.0/len(boroughs.keys()) for k in range(len(boroughs.keys()) + 2)]
for borough, borough_num in boroughs.iteritems():
    ax.scatter(zip_pop_count['population'][zip_pop_count['borough'] == borough_num],
               zip_pop_count['complaints'][zip_pop_count['borough'] == borough_num],
               lw = 0,
               c = cm.Dark2(colors[borough_num]),
               label = borough,
               s = 30,
               alpha = .8)
ax.set_xlabel('2010 census population')
ax.set_ylabel('Number of 311 complaints')
ax.set_title('311 Complaints by Zip Code Jun/1/2013-Aug/31/2013')
xlims = ax.get_xlim()
ax.set_xlim(xlims[0]/4, xlims[1])
ylims = ax.get_ylim()
ax.set_ylim(ylims[0]/2.5, ylims[1])
ax.legend(loc = 2)
plt.show()


# In[ ]:



