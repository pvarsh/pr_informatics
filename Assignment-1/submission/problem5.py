########################################
#### Principles of Urban Informatics
#### Peter Varshavsky
#### Assignment 1
#### Problem 5
########################################

import csv
import sys
import time
from time import strptime
from time import strftime

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
    for item in dayCounts:
        print '%s == %d' %(item[0], item[1])


def main(argv):
    if len(argv) == 1:
        dayWeekCount(argv[0])
    else:
        print "Invalid number of arguments. Call format: 'python problem1.py data_file.csv n'"

if __name__ == "__main__":
    main(sys.argv[1:])
