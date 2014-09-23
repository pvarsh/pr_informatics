##################################
# Principles of Urban Informatics
# Assignment 3: Problem 1
# Peter Varshavsky
##################################

import sys
import csv
from datetime import datetime

def problem1(fileName):
    tweets = []
    fmtIn = "%a %b %d %H:%M:%S %Z %Y"
    fmtOut = "%B %d %Y, %H:%M:%S"
    maxDate = datetime.strptime("Dec 01 1900", "%b %d %Y")
    minDate = datetime.strptime("Dec 01 5000", "%b %d %Y") 
    count = 0
    with open(fileName, 'r') as f:
         reader = csv.reader(f)
         for line in reader:
             count += 1
             tweetDateTime = datetime.strptime(line[1], fmtIn)
             if tweetDateTime < minDate:
                 minDate = tweetDateTime
             if tweetDateTime > maxDate:
                 maxDate = tweetDateTime
    print 'There were %d tweets between %s and %s' %(count, datetime.strftime(minDate, fmtOut),datetime.strftime(maxDate, fmtOut))

def main(argv):
    tweets = problem1(argv[0])
    
if __name__ == '__main__':
    main(sys.argv[1:])
