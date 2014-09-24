##################################
# Principles of Urban Informatics
# Assignment 3: Problem 5
# Peter Varshavsky
##################################

import sys
import csv
from datetime import datetime

def problem5(fileName):
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

def buildTagDict(filename):
    hashtags = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            for tag in line[4:]:
                if tag in hashtags.keys():
                    hashtags[tag] += 1
                else:
                    hashtags[tag] = 1
    return hashtags

def buildTimeDict(filename):
    times = {}
    
    fmtIn = "%a %b %d %H:%M:%S %Z %Y"
    fmtOut = "%B %d %Y, %H:%M:%S"
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            tweetTime = datetime.strptime(line[1], fmtIn)
            if tweetTime in times.keys():
                times[tweetTime] += 1
            else:
                times[tweetTime] = 1
    busyTime, count = max(times.iteritems(), key = lambda t: t[1])
    print datetime.strftime(busyTime, fmtOut) + " with %d tweets" %count
    return times    

def main(argv):
    
    buildTimeDict(argv[0])


    #tags = buildTagDict(argv[0]) 
    #taglist = [(tag, count) for tag, count in tags.iteritems()]
    
    #taglist = sorted(taglist, key = lambda t: (-t[1], t[0]))
    
    #for i in range(min(10, len(taglist))):
    #    print taglist[i][0] + ', ' + str( taglist[i][1])

if __name__ == '__main__':
    main(sys.argv[1:])
