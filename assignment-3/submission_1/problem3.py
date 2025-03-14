##################################
# Principles of Urban Informatics
# Assignment 3: Problem 3
# Peter Varshavsky
##################################

import sys
import csv
from datetime import datetime

def problem3(fileName):
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

def buildHashtagSet(filename):
    hashtags = set()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            for tag in line[4:]:
                hashtags.add(tag)
    return hashtags

    

def main(argv):
    tags1 = buildHashtagSet(argv[0])
    tags2 = buildHashtagSet(argv[1])
    commonTags = tags1.intersection(tags2)
    
    a = list(commonTags)
    for tag in sorted(a):
        print tag

if __name__ == '__main__':
    main(sys.argv[1:])
