########################################
#### Principles of Urban Informatics
#### Assignment 1
#### Peter Varshavsky
########################################

import csv
import os
import time
from time import strptime
from time import strftime

### Problem 1

filename = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/Assignment-1/data/sample_data_problem_1.csv"

def complaintRange(filename):

    time_max = strptime('00', '%y') 
    time_min = strptime('9999', '%Y')
    complaintCounter = 0
    
    with open(filename) as f:
        csvf = csv.reader(f, delimiter=',')
        csvf.next() # skip header
        for line in csvf:
            complaintCounter += 1
            print line[1]
            lineTime = strptime(line[1], '%m/%d/%Y %I:%M:%S %p')
            if lineTime < time_min:
                time_min = lineTime
            if lineTime > time_max:
                time_max = lineTime
    print str(complaintCounter) + " complaints between " + strftime('%m/%d/%Y %H:%M:%S', time_min) + " and " + strftime('%m/%d/%Y %H:%M:%S', time_max)


def complaintTypes(filename):

    typesDict = {}
    
    with open(filename) as f:
        csvf = csv.reader(f, delimiter = ',')
        csvf.next() # skip header
        for line in csvf:
            if line[5] in typesDict.keys():
                typesDict[line[5]] += 1
            else:
                typesDict[line[5]] = 1
    for item in typesDict.keys():
        print item + " with " + str(typesDict[item]) + " complaints"
        
def complaintTypesSorted(filename):
    typesDict = {}
    
    with open(filename) as f:
        csvf = csv.reader(f, delimiter = ',')
        csvf.next() # skip header
        for line in csvf:
            if line[5] in typesDict.keys():
                typesDict[line[5]] += 1
            else:
                typesDict[line[5]] = 1

    typesList = [(x, typesDict[x]) for x in typesDict]
    typesList = sorted(typesList, key = lambda x: x[0])
    typesList = sorted(typesList, key = lambda x: x[1], reverse = True)
 
    print typesList

    
        
    
#complaintRange(filename)
#complaintTypes(filename)
complaintTypesSorted(filename)


