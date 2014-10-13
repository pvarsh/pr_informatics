import math


# Functions for students to implement.


# Performs search in unsorted L.
# L might not be sorted. Can't use sorting to solve this.
def searchGreaterNotSorted(L, v):
  return sum([1 for x in L if x > v])
  #return -1

# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
  length = len(L)
  for i in xrange(length):
    if L[i] > v:
       break
  if i == length - 1 and L[i] <= v:
    return 0
  else:
    return length-i


def binNoSearch(L, v):
  # binary No Search (returns value whether or not search successful to be used     in countGreater()
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

def searchGreaterBinSearch(L, v):
  if len(L) == 0:
    return 0
  ## using binNoSearch()
  splitIndex = binNoSearch(L, v)
  if L[splitIndex] > v:
    return len(L) - splitIndex
  elif L[splitIndex] < v:
    return len(L) - splitIndex - 1
  else:
    while splitIndex < len(L) and L[splitIndex] == v:
      splitIndex += 1
    if splitIndex == len(L): # if repeated value reached end of list like [1,2,3    ,3,3] 
      return 0
    else:
      return len(L) - splitIndex

# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
  return searchGreaterBinSearch(L, v1) - searchGreaterBinSearch(L, v2) 
