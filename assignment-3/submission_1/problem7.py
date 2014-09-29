#################################
# Principles of Urban Informatics
# Assignment 3: Problem 7
# Peter Varshavsky
##################################

import sys
import csv
from datetime import datetime


def buildUserCount(filename):
    users = {}
    maxDate = datetime.strptime("1900", "%Y")
    minDate = datetime.strptime("5000", "%Y")
    
    fmtIn = "%a %b %d %H:%M:%S %Z %Y"
    fmtOut = ""
  
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            # date compare
            date = datetime.strptime(line[1], fmtIn) 
            if date < minDate:
                minDate = date
            if date > maxDate:
                maxDate = date
            if line[0] in users:
                users[line[0]] += 1
            else:
                users[line[0]] = 1
    return users, (minDate, maxDate)

def main(argv):
   
    # problem 6 
    #times, granularity = buildTimeDict(argv[0], "hour")
    #problem6(times)
     
    # problem 7
    fmtOut = "%B %d %Y, %H:%M:%S"
    users, dateRange = buildUserCount(argv[0])
    chatterBox, maxTweets = max(users.iteritems(), key = lambda t: t[1])
    chatterBox = [user for user, nTweets in users.iteritems() if nTweets == maxTweets]
    print "%s tweeted the most" %sorted(chatterBox)[0]
    print "Dataset range: %s and %s" %(datetime.strftime(dateRange[0], fmtOut), datetime.strftime(dateRange[1], fmtOut))
    
    # printing all users and their counts for problem 7
    #userList = sorted([user for user, nTweets in sorted(users.iteritems(), key = lambda t: t[1])])
    #for user, nTweets in users.iteritems():
    #    print user, nTweets


    #tags = buildTagDict(argv[0]) 
    #taglist = [(tag, count) for tag, count in tags.iteritems()]
    
    #taglist = sorted(taglist, key = lambda t: (-t[1], t[0]))
    
    #for i in range(min(10, len(taglist))):
    #    print taglist[i][0] + ', ' + str( taglist[i][1])

if __name__ == '__main__':
    main(sys.argv[1:])
