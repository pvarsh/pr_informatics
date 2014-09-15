########################################
#### Principles of Urban Informatics
#### Peter Varshavsky
#### Assignment 1
#### Problem 7
########################################

import csv
import sys
import time
from time import strptime
from time import strftime

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

def main(argv):
    if len(argv) == 2:
        print78(problem7(argv[0], argv[1]))
    else:
        print "Invalid number of arguments. Call format: 'python problem1.py data_file.csv zip_borough.csv'"

if __name__ == "__main__":
    main(sys.argv[1:])
