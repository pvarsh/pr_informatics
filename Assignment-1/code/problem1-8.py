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
filename6 = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/Assignment-1/data/sample_data_problem_6a.csv"

filename7 = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/Assignment-1/data/sample_data_problem_7.csv"

filename8 = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/Assignment-1/data/sample_data_problem_8.csv"
filename_borough = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/Assignment-1/data/zip_borough.csv" 

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
        
def dayWeekCount(filename):

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # for sorting by day of week
    weekdaysDict = {x:y for x, y in zip(weekdays, range(7))}
    
    dayDict = {x: 0 for x in weekdays}
    with open(filename) as f:
        csvf = csv.reader(f)
        csvf.next()
        for line in csvf:
            lineTime = strptime(line[1], '%m/%d/%Y %I:%M:%S %p')
            dayDict[strftime('%A', lineTime)] += 1

    dayCounts = [(x, dayDict[x]) for x in dayDict]
    dayCounts = sorted(dayCounts, key = lambda t: weekdaysDict[t[0]])

    # output
    print "\nPROBLEM 5:"
    for item in dayCounts:
        print '%s == %d' %(item[0], item[1])


def agencyZipCount(filename):
    #{agency: {zip: count}} 3 7
    agencyDict = {}

    # read file and build a dictionary of dictionaries of the form
    # {agency: {zip: count}}
    with open(filename) as f:
        csvf = csv.reader(f)
        csvf.next() #skipping header
        for line in csvf:
            if line[3] in agencyDict.keys():
                if line[7] in agencyDict[line[3]].keys():
                    agencyDict[line[3]][line[7]] += 1
                else:
                    agencyDict[line[3]][line[7]] = 1
            else:
                agencyDict[line[3]] = {line[7]: 1}

    # change the dictionary to form:
    # {agency: (maxcount, [zips])}
    agencyCountZip = {}
    for agency in agencyDict:
        templist = [(count, zip) for zip, count in agencyDict[agency].iteritems()]
        m = max(templist, key = lambda t: t[0])[0]
        agencyCountZip[agency] = (m, [item[1][1] for item in enumerate(templist) if item[1][0] == m])

    return agencyCountZip

def printProblem6(agencyCountZip):
    for agency in agencyCountZip:
        zips = ' '.join(agencyCountZip[agency][1])
        print agency, zips, agencyCountZip[agency][0]
        
                
            
def problem7(filename7, filename_borough):
    
    zip_borough = {}
    boroughs = [] 
    with open(filename_borough) as f:
        csvf = csv.reader(f) 
        csvf.next() # skip first line
	for line in csvf:
            zip_borough[line[0]] = line[1]
            if line[1] not in boroughs:
                boroughs.append(line[1])
    #print boroughs
    #print zip_borough

    borough_counts = {borough: 0 for borough in boroughs}
    with open(filename7) as f:
        csvf = csv.reader(f)
        csvf.next() # skip first line
        for line in csvf:
            if line[7] in zip_borough.keys():
                borough_counts[zip_borough[line[7]]] += 1
    borough_counts = sorted([(borough, count) for borough, count in borough_counts.iteritems()], key = lambda t: t[1], reverse = True)
    return borough_counts 

def print78(borough_counts):
    for pair in borough_counts:
        print pair[0].title(), "with", pair[1], "complaints"

#complaintRange(filename)
#complaintTypes(filename)
#complaintTypesSorted(filename)
#problem3(filename)
#problem4(filename, 2)
#dayWeekCount(filename)
#ACZ = agencyZipCount(filename6)
#printProblem6(ACZ)
counts = problem7(filename8, filename_borough)
print78(counts)
