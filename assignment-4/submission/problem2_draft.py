import numpy as np
import math
from datetime import datetime


#x = np.random.randint(0,100000, 10000000)
#v = 200



# Functions for students to implement.

# Performs search in unsorted L.
# L might not be sorted. Can't use sorting to solve this.
def searchGreaterNotSorted(L, v):
  return sum([1 for x in L if x > v])
  #return -1

def sgns2(L, v):
  counter = 0
  for item in L:
    if item > v:
      counter += 1
  return counter 

### Testing two versions of problem 2.a.
#now1 = datetime.now()
#s1 = searchGreaterNotSorted(x, v)
#delta1 = datetime.now() - now1
#
#now2 = datetime.now()
#s2 = sgns2(x, v)
#delta2 = datetime.now() - now2
#
#print delta1
#print delta2
#print s1, s2


# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
  length = len(L)
  for i in xrange(length):
    if L[i] > v:
       break
  return length-i

#L = np.linspace(10, 1000, 1000)
#v = 600
#
#now1 = datetime.now()
#out1 = searchGreaterSorted(L, v)
#delta1 = datetime.now() - now1
#now2 = datetime.now()
#out2 = searchGreaterNotSorted(L, v)
#delta2 = datetime.now() - now2
#
#print out1, out2
#print delta1
#print delta2

# Performs binary search in sorted L (ascending order).
def searchGreaterBinSearch(L, v):
  return -1

def binSearch(L, v, iMin, iMax):
  if iMin > iMax:
    return None
  else:
    iMid = iMin + (iMax - iMin)/2
    if L[iMid] > v:
      return binSearch(L, v, iMin, iMid - 1)
    elif L[iMid] < v:
      return binSearch(L, v, iMid + 1, iMax)
    else:
      return iMid

def findFirstBin(L, v):
  imin = 0
  imax = len(L) - 1
  firstOccurrence = -1 
  while imin <= imax:
    #print "######"
    imid = imin + math.ceil((imax - imin)/2.0) # + 1
    imid = int(imid)
    #print "Inside while: imin:%d, imax:%d, imid:%d, L[imid]:%d" %(imin, imax, imid, L[imid]), L[imin:imax+1]
    #raw_input("Press enter:")
    if v <= L[imid]:
      if v == L[imid]:
        firstOccurrence = imid
        #print "firstOccurrence: ", firstOccurrence
      imax = imid-1
      #print "imax: %d" %imax
    elif v > L[imid]:
      imin = imid + 1
  return firstOccurrence


def binSearchIt(L, v):
  start = 0
  end = len(L) - 1
  while start < end:
    middle = start + math.ceil((end - start)/2.0)
    middle = int(middle)
    if v < L[middle]:
      end = middle - 1
    elif v > L[middle]:
      start = middle + 1
    elif v == L[middle]:
      return middle
  return middle 

def binNoSearch(L, v):
  # binary No Search (returns value whether or not search successful to be used in countGreater()
  # returns either:
  #   -index of an occurrence of v in L
  #   -index of where the binary division terminated
  #      which can be:
  #      - equal to v
  #      - first element greater than v
  #      - last element less than v 

  length = len(L)
  start = 0
  end = length - 1
  while start < end:
    middle = start + int(math.floor((end - start)/2))
    if v == L[middle]:
      return middle
    elif v < L[middle]:
      end = middle - 1
    else:
      start = middle + 1
  return start

def countGreater(L, v):
  # using binNoSearch()
  
  splitIndex = binNoSearch(L, v)
  #print "splitIndex: %d for v = %d" %(splitIndex,v)
  if L[splitIndex] > v:
    return len(L) - splitIndex
  elif L[splitIndex] < v:
    return len(L) - splitIndex - 1
  else:
    while splitIndex < len(L) and L[splitIndex] == v:
      splitIndex += 1
    if splitIndex == len(L): # if repeated value reached end of list like [1,2,3,3,3] 
      return 0
    else:
      return len(L) - splitIndex 


# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
  return -1
