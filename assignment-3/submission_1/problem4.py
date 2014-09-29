##################################
# Principles of Urban Informatics
# Assignment 3: Problem 4
# Peter Varshavsky
##################################
import timeit
import sys
import csv
from datetime import datetime


def buildTagDict(filename):
    hashtags = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            for tag in line[4:]:
                if tag in hashtags:
                    hashtags[tag] += 1
                else:
                    hashtags[tag] = 1
    return hashtags

#def buildTagDict(filename):
#    hashtags = {}
#    with open(filename, 'r') as f:
#        print {tag:1 for tag in line[4:] for line in csv.reader(f)}

def main(argv):
    tags = buildTagDict(argv[0])
    taglist = [(tag, count) for tag, count in tags.iteritems()]
   
    taglist = sorted(taglist, key = lambda t: (-t[1], t[0]))
     
    for i in range(min(10, len(taglist))):
        print taglist[i][0] + ', ' + str( taglist[i][1])

if __name__ == '__main__':
  main(sys.argv[1:])

#timeit.timeit('main(["sample_data_problem_4.txt"])', number = 10)
