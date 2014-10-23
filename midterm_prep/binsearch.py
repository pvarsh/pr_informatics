##### Review of binary search #####
##### An attempt to write binary search from scratch without references ####
import math
import random


### Recursive binary search
def binsearch(x, y, imin = 0, imax = -1):
  if imax == -1:
    imax = len(x) - 1
  if imin == imax:
    if x[imin] == y:
      return imin
    else:
      return -1
  imid = int(imin + math.floor(float(imax - imin)/2))
  if x[imid] == y:
    return imid
  elif x[imid] > y:
    found = binsearch(x, y, imin, imid)
  elif x[imid] < y:
    found = binsearch(x, y, imid+1, imax)
  return found

### Iterative binary search
def binitersearch(x, y):
  imin = 0
  imax = len(x) - 1
  imid = imin + int(math.floor(float(imax - imin)/2))  

  while imin < imax:
    if y == x[imid]:
      break
    elif y < x[imid]:
      imax = imid
    else:
      imin = imid + 1
    imid = imin + int(math.floor(float(imax - imin)/2))  

  if x[imid] == y:
    return imid
  else:
    return -1    


### Parameters for list to be searched
xmin = 0
xmax = 20
n = 11
random.seed(1234)
x = [random.randint(xmin, xmax) for _ in range(n)]
x.sort()
print x

### Run search on a range of values
for num in range(xmin - 1, xmax + 2):
  print "%d found: %d" %(num, binsearch(x, num))
  print "%d found: %d" %(num, binitersearch(x, num))


