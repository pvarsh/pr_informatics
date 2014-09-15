########################################
#### Principles of Urban Informatics
#### Peter Varshavsky
#### Assignment 1
#### Problem 3
########################################

import csv
import sys
import time
from time import strptime
from time import strftime

def printComplaintCounts(complaintList):
    for item in complaintList:
        print item[0] + ' with ' + str(item[1]) + ' complaints'

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

def complaintTypesSorted(filename):
    typesDict = buildComplaintDict(filename)
    
    typesList = [(x, typesDict[x]) for x in typesDict]

    # sorting twice to sort first by complaint count and then by agency
    typesList = sorted(typesList, key = lambda x: x[0])
    typesList = sorted(typesList, key = lambda x: x[1], reverse = True)

    return typesList

def main(argv):
    if len(argv) == 1:
        printComplaintCounts(complaintTypesSorted(argv[0]))
    else:
        print "Invalid number of arguments. Call format: 'python problem1.py data_file.csv'"

if __name__ == "__main__":
    main(sys.argv[1:])
