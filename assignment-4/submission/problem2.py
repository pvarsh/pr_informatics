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

L = np.linspace(10, 1000, 1000)
v = 600

now1 = datetime.now()
out1 = searchGreaterSorted(L, v)
delta1 = datetime.now() - now1
now2 = datetime.now()
out2 = searchGreaterNotSorted(L, v)
delta2 = datetime.now() - now2

print out1, out2
print delta1
print delta2
# Performs binary search in sorted L (ascending order).
def searchGreaterBinSearch(L, v):
  return -1

#def bisectGreater(L, v, indStart = 0):
#  # return the position of right-most element less than or equal to v
#  # work on enumerated list
#  
#  length = len(L)
#  half  = len(L)/2
#  print "indStart %d" %indStart
#  print "L:", L 
#  raw_input("Press something and enter:")
#  if L[half] == v:
#    return indStart + half
#  elif L[half] > v and length > 1:
#    return indStart + bisectGreater(L[0:half], v, 0)
#  elif L[half] < v and length > 1:
#    return indStart + bisectGreater(L[half: ], v, half)
#  elif length == 1 and L[half] != v:
#    return None

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

def binSearchIt(L, v):
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

def lastOccurrenceBin(L, v):
  imin = 0
  imax = len(L) - 1
  while imin <= imax:
    imid = imin + math.ceil(imax - imin/2.0)
    imid = int(imid)
    if v >= L[imid]:
      if v == L[imid]:
        lastOccurrence = imid
    imax = imid - 1


def createSorted(length):
  return sorted(np.random.randint(10, 30, length))

def testFound(L, v, i):
  if i == -1 and v not in L:
    return True, "Not found"
  elif L[i] == v:
    return True, "Found"
  else:
    return False, "Search didn't work"

def testSortFun(nlists, lengthLists):
  for n in range(nlists):
    thisLength = lengthLists + np.random.randint(0,2)
    L = createSorted(thisLength)
    v = np.random.randint(10,30)
    foundIndex = binSearchIt(L, v)
    success, ifFound = testFound(L, v, foundIndex)
    print success, "%s %d in" %(ifFound, v), L
 

testSortFun(nlists = 20, lengthLists = 10)






  
##L = np.linspace(0, 200, 10)
#L = [1,2,3,3,5,6]
#for v in L:
##v = 1
#  print "Looking for %d" %v
##bisection = binSearch(L, v, 0, len(L)-1)
##print "Found at index %d" %bisection
#  first = binSearchIt(L, v)
#  print "Found first:", first


# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
  return -1
