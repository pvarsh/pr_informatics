#################################
# Principles of Urban Informatics
# Assignment 3: Problem 6
# Peter Varshavsky
##################################

import sys
import csv
from datetime import datetime



def buildTimeDict(filename, granularity):
    times = {}
    
    fmtIn = "%a %b %d %H:%M:%S %Z %Y"
    fmtOut = "%B %d %Y, %H:%M:%S"
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            # if granularity == 'second', hash the datetime object directly
            tweetTime = line[1] # was tweetTime = datetime.strptime(line[1], fmtIn)
            # if granularity == 'hour', extract year, month, date, hour from dateTime object and hash
            if granularity == "hour":
                tweetTime = tweetTime[4:13] + tweetTime[24:]
            if tweetTime in times:
                times[tweetTime] += 1
            else:
                times[tweetTime] = 1
    #busyTime, count = max(times.iteritems(), key = lambda t: t[1])
    #print busyTime + " with %d tweets" %count
    #print datetime.strftime(busyTime, fmtOut) + " with %d tweets" %count
    return (times, granularity)    


def problem6(times):
    busyTime, count = max(times.iteritems(), key = lambda t: t[1])
    busyTime = datetime.strptime(busyTime, "%b %d %H%Y")
    print datetime.strftime(busyTime, "%B %d %Y, %Hh") + " with %d tweets" %count

def main(argv):
    
    times, granularity = buildTimeDict(argv[0], "hour")
    problem6(times)
    

    #tags = buildTagDict(argv[0]) 
    #taglist = [(tag, count) for tag, count in tags.iteritems()]
    
    #taglist = sorted(taglist, key = lambda t: (-t[1], t[0]))
    
    #for i in range(min(10, len(taglist))):
    #    print taglist[i][0] + ', ' + str( taglist[i][1])

if __name__ == '__main__':
    main(sys.argv[1:])
