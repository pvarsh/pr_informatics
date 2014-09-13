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

    typesDict = buildComplaintDict(filename)

    print "\nPROBLEM 2: "
    printComplaintCounts([(x, typesDict[x]) for x in typesDict])
        
def complaintTypesSorted(filename):
    typesDict = buildComplaintDict(filename)

    typesList = [(x, typesDict[x]) for x in typesDict]
    typesList = sorted(typesList, key = lambda x: x[0])
    typesList = sorted(typesList, key = lambda x: x[1], reverse = True)

    return typesList

def buildComplaintDict(filename):
    typesDict = {}

    with open(filename) as f:
        csvf = csv.reader(f, delimiter = ',')
        csvf.next() # skip header
        for line in csvf:
            if line[5] in typesDict.keys():
                typesDict[line[5]] += 1
            else:
                typesDict[line[5]] = 1
    return typesDict

def topComplaints(filename, n):
    typesList = complaintTypesSorted(filename)
    if n >= 0:
        printComplaintCount(typesList[0:n])
    else:
        print "Must request a non-negative number of services"

def printComplaintCounts(complaintList):
    for item in complaintList:
        print item[0] + ' with ' + str(item[1]) + ' complaints'
            

def problem3(filename):
    print "\nPROBLEM 3:"
    printComplaintCounts(complaintTypesSorted(filename))

def problem4(filename, n):
    print "\nPROBLEM 4:"
    printComplaintCounts(complaintTypesSorted(filename)[0:n])
        

#complaintRange(filename)
complaintTypes(filename)
complaintTypesSorted(filename)
problem3(filename)
problem4(filename, 2)


