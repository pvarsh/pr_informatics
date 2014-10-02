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
  print "splitIndex: %d for v = %d" %(splitIndex,v)
  if L[splitIndex] > v:
    return len(L) - splitIndex
  elif L[splitIndex] < v:
    return len(L) - splitIndex - 1
  else:
    while splitIndex < len(L) and L[splitIndex] == v:
      splitIndex += 1
    if splitIndex == len(L):
      return 0
    else:
      return len(L) - splitIndex 

L = [1,3,5,5,8,8]
#L = [1,2,3,3,3]
print L
#print countGreater(L, 3)

for v in range(0, 11):
  print "%d elements greater than %d" %(countGreater(L, v), v)
print countGreater(L, v)

#L = [1, 3, 5, 7, 9]
#print L
#for v in range(11):
#  splitAt = binNoSearch(L, v)
#  print "split at %d for v=%d" %(splitAt, v) 
#print binNoSearch(L, v)

def countGreater(L, v):
  ind = binSearchIt(L, v)
  print "val: %d, ind: %d" %(v, ind), L
  while L[ind] == v and ind < len(L):
    ind += 1
  if ind == len(L):
    return 0
  else:
    return len(L) - (ind)
  

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
 

#testSortFun(nlists = 20, lengthLists = 10)

def testCountGreater(nlists, lengthLists):
  for n in range(nlists):
    thisLength = lengthLists + np.random.randint(0,2)
    L = createSorted(thisLength)
    v = np.random.randint(10,30)
    cg = countGreater(L, v)
    print "%d values greater than %d in list" %(cg, v), L

#testCountGreater(nlists = 20, lengthLists = 10)



  
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
