#!/usr/bin/python

from datetime import datetime
import sys
import csv
import heapq

#IN HEAP LOOK AT KEY: TOO MANY SORTINGS
#starttime = datetime.now()

def solution(filename):
  tags = {} 
  with open(filename) as fl:
    reader = csv.reader(fl)
    for row in reader:
      for htag in row[4:]:
        if htag in tags:
          tags[htag]+=1
        else:
          tags[htag]=1
   
    tags = dict((tag,tags[tag]) for tag in heapq.nlargest(10, sorted(tags), key=tags.get))
    for item in sorted(tags.iteritems(), key = lambda x:(-x[1],x[0][1]), reverse=False):
      print "%s, %s" %(item[0], item[1])

if __name__ == '__main__':
  solution(sys.argv[1])
  

#print datetime.now()-starttime
