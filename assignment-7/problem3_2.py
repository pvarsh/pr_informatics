
# coding: utf-8

# In[1]:

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
import matplotlib.cm as cm

### settings
#get_ipython().magic(u'matplotlib inline')


####### Read 311 data

# In[2]:

### read data
### reading is slow due to parsing two columns as datetime
in_file = "311_Service_Requests_from_2010_to_Present.csv"
with open(in_file, 'r') as f:
    df = pd.read_csv(f, 
                     index_col = ['Unique Key'],
                     dtype = {'Incident Zip': str})
#                      parse_dates=['Created Date', 'Closed Date'],
#                      )


####### Cleaning zip codes

# In[3]:

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

# In[4]:

zipcode_file = "zipCodePopulationData.csv"
with open(zipcode_file, 'r') as f:
    zipcodes = pd.read_csv(f, dtype = {'Zip Code ZCTA': str, '2010 Census Population': int})
zipcodes['Zip Code ZCTA'] = zipcodes['Zip Code ZCTA'].astype(str).apply(lambda x: x.zfill(5))


####### Which agencies got most complaints in each zip code

# In[5]:

### group by agency and zip
grouped_zip_agency = df['Incident Zip'].groupby([df['Incident Zip'], df['Agency']])
### count per agency per zip code
zip_agency_counts = grouped_zip_agency.count()
### agencies with the most complaints per zip code, ties resolved by ordering in dataframe
zip_agencies_dict = {key: zip_agency_counts[key].idxmax() for key in zip_agency_counts.keys().levels[0]}


####### Complaint counts per zip code

# In[6]:

### group and count
grouped_zip = df['Incident Zip'].groupby(df['Incident Zip'])
zip_counts = pd.DataFrame(grouped_zip.count())
### rename
zip_counts.columns = ['Number of Complaints']
### zips as column
zip_counts['Incident Zip'] = zip_counts.index
### add agency from dictionary
zip_counts['Agency'] = zip_counts['Incident Zip']
zip_counts.replace({'Agency': zip_agencies_dict}, inplace = True)


####### Merge

# In[7]:

zip_pop_count = pd.merge(zipcodes, zip_counts, left_on ='Zip Code ZCTA', right_on='Incident Zip')
zip_pop_count = zip_pop_count[['Incident Zip', '2010 Census Population', 'Number of Complaints', 'Agency']]
zip_pop_count.columns = ['zip', 'population', 'complaints', 'agency']


# In[8]:

### agencies to be identified on plot
agencies = ['NYPD','DOT','DOB','TLC','DPR']
### numbering of agencies for color coding
agency_color_codes = {ag : num for num, ag in enumerate(agencies)}
### list of all agencies in 311 file
all_agencies = list(df['Agency'])
### adding other agencies to color code dictionary for 'other' color
# for agency in all_agencies:
#     if agency not in agencies:
#         agency_color_codes[agency] = len(agencies)


####### Plot

# In[17]:

fig, ax = plt.subplots(figsize=(10, 5))
colors = [k * 1.0/(len(agencies) + 2) for k in range(len(agencies) + 2)]
pattern = '|'.join(agencies)
### plotting 'other' agencies
ax.scatter(zip_pop_count['population'][~zip_pop_count['agency'].str.contains(pattern)],
           zip_pop_count['complaints'][~zip_pop_count['agency'].str.contains(pattern)],
           label = 'Other',
           color = cm.Accent(colors[len(agencies) + 1]),
           alpha = .2,
           s = 20)
### plotting agencies of interest
for agency, agency_num in agency_color_codes.iteritems():
    ax.scatter(zip_pop_count['population'][zip_pop_count['agency'] == agency],
               zip_pop_count['complaints'][zip_pop_count['agency'] == agency],
               lw = 0,
               c = cm.Dark2(colors[agency_num]),
               label = agency,
               s = 40,
               alpha = .7)
ax.set_xlabel('2010 census population\nColors indicate which agency received the most complaints in each zip code')
ax.set_ylabel('Number of 311 complaints for all agencies')
ax.set_title('311 Complaints by Zip Code by Agency')
xlims = ax.get_xlim()
ax.set_xlim(xlims[0]/4, xlims[1])
ylims = ax.get_ylim()
ax.set_ylim(ylims[0]/2.5, ylims[1])
ax.legend(loc = 2)
plt.show()


# In[9]:



