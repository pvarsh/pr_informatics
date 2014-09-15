########################################
#### Principles of Urban Informatics
#### Peter Varshavsky
#### Assignment 1
#### Problem 6
########################################

import csv
import sys
import time
from time import strptime
from time import strftime

def agencyZipCount(filename):
    #{agency: {zip: count}} 3 7
    agencyDict = {}

    # read file and build a dictionary of dictionaries of the form
    # {agency: {zip: count}}
    with open(filename) as f:
        csvf = csv.reader(f)
        csvf.next() #skipping header
        for line in csvf:
            if len(line[7]) == 5: #testing that zip code string is correct length
                if line[3] in agencyDict.keys():
                    if line[7] in agencyDict[line[3]].keys():
                        agencyDict[line[3]][line[7]] += 1
                    else:
                        agencyDict[line[3]][line[7]] = 1
                else:
                    agencyDict[line[3]] = {line[7]: 1}

    # change the dictionary to form:
    # {agency: (maxcount, [zips])}
    agencyCountZip = []
    for agency in agencyDict:
        templist = [(count, zip) for zip, count in agencyDict[agency].iteritems()]
        m = max(templist, key = lambda t: t[0])[0]
        agencyCountZip.append((agency, m, [item[1][1] for item in enumerate(templist) if item[1][0] == m]))
    agencyCountZip = sorted(agencyCountZip, key = lambda t: t[0])
    
    return agencyCountZip

def printProblem6(agencyCountZip):
    for agency in agencyCountZip:
        zips = ' '.join(agency[2])
        print agency[0], zips, agency[1]


def main(argv):
    if len(argv) == 1:
        printProblem6(agencyZipCount(argv[0]))
    else:
        print "Invalid number of arguments. Call format: 'python problem1.py data_file.csv n'"

if __name__ == "__main__":
    main(sys.argv[1:])
