#!/usr/bin/python

import csv,sys

res=dict()
with open(sys.argv[1]) as csvfl:
  cmplreader = csv.DictReader(csvfl)
  for row in cmplreader:
    key = row['Complaint Type']
    if key in res:
     res[key]+=1
    else:
     res[key]=1
  csvfl.close()

for key in res:
 print key + ' with ' + str(res[key])+ ' complaints'
