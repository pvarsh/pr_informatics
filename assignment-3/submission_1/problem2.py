##################################
# Principles of Urban Informatics
# Assignment 3: Problem 2
# Peter Varshavsky
##################################

import sys
import csv
from datetime import datetime

def problem2(fileName):
    fmtIn = "%a %b %d %H:%M:%S %Z %Y"
    fmtOut = "%B %d %Y, %H:%M:%S"
    maxDate = datetime.strptime("Dec 01 1900", "%b %d %Y")
    minDate = datetime.strptime("Dec 01 5000", "%b %d %Y") 
    count = 0
    users = {}
    with open(fileName, 'r') as f:
         reader = csv.reader(f)
         for line in reader:
             count += 1
             users[line[0]] = ''
             tweetDateTime = datetime.strptime(line[1], fmtIn)
             if tweetDateTime < minDate:
                 minDate = tweetDateTime
             if tweetDateTime > maxDate:
                 maxDate = tweetDateTime
    print '%d users tweeted between %s and %s' %(len(users), datetime.strftime(minDate, fmtOut),datetime.strftime(maxDate, fmtOut))

def main(argv):
    tweets = problem2(argv[0])
    
if __name__ == '__main__':
    main(sys.argv[1:])
