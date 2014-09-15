########################################
#### Principles of Urban Informatics
#### Peter Varshavsky
#### Assignment 1
#### Problem 1
########################################

import csv
import sys
import time
from time import strptime
from time import strftime


def main(argv):

    if len(argv) == 1:
        complaintCounter, time_min, time_max = readFileProblem1(argv[0])
        print_problem1(complaintCounter, time_min, time_max)
    else:
        print "Invalid number of arguments. Call format: 'python problem1.py data_file.csv'"
    
    #print str(complaintCounter) + " complaints between " + strftime('%m/%d/%Y %H:%M:%S', time_min) + " and " + strftime('%m/%d/%Y %H:%M:%S', time_max)

def readFileProblem1(filename):

    # initializing min and max times
    time_max = strptime('00', '%y') 
    time_min = strptime('9999', '%Y')
    complaintCounter = 0

    # reading file and computing max, min, counter
    with open(filename) as f:
        csvf = csv.reader(f, delimiter=',')
        csvf.next() # skip header
        for line in csvf:
            complaintCounter += 1
            lineTime = strptime(line[1], '%m/%d/%Y %I:%M:%S %p')
            if lineTime < time_min:
                time_min = lineTime
            if lineTime > time_max:
                time_max = lineTime
    return complaintCounter, time_min, time_max
    
def print_problem1(complaintCounter, time_min, time_max):
    print str(complaintCounter) + " complaints between " + strftime('%m/%d/%Y %H:%M:%S', time_min) + " and " + strftime('%m/%d/%Y %H:%M:%S', time_max)

if __name__ == "__main__":
    main(sys.argv[1:])

