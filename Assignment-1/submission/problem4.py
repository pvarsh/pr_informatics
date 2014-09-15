########################################
#### Principles of Urban Informatics
#### Peter Varshavsky
#### Assignment 1
#### Problem 4
########################################

import csv
import sys
import time
from time import strptime
from time import strftime

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

def printComplaintCounts(complaintList):
    for item in complaintList:
        print item[0] + ' with ' + str(item[1]) + ' complaints'

def main(argv):
    if len(argv) == 2:
        n = int(argv[1])
        filename = argv[0]
        printComplaintCounts(complaintTypesSorted(filename)[0:n])
    else:
        print "Invalid number of arguments. Call format: 'python problem1.py data_file.csv n'"

if __name__ == "__main__":
    main(sys.argv[1:])
