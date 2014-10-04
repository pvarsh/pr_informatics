# Functions for students to implement.

naive = []
def buildNaive(points,n):
    del naive[:] #erasing previous data

    #your code here
    for point in points:
        naive.append(point)
    #print points[0:10]
    return None

def createSubdivision(n):
    subDiv = [0 + round(float(k)/n, 7) for k in range(n)]
    subDiv.append(1.0)
    return subDiv

def findSubdivision(subDivision, point):
    wall = 0
    while subDivision[wall] <= point[0] and subDivision[wall] != 1.0:
        wall += 1
    wall = wall - 1
    return wall

def findLeftWall(subDivision, point):
    wall = 0
    while subDivision[wall] <= point[0] and subDivision[wall] != 1.0:
        wall += 1
    wall = wall - 1
    return wall

def findRightWall(subDivision, point):
    wall = len(subDivision) - 2
    while subDivision[wall] > point[0] and subDivision[wall] != 0:
        wall -= 1
    return wall

onedim = []

def buildOneDim(points,n):
    del onedim[:] #erasing previous data

    #your code here
    onedim.append(createSubdivision(n))
    for k in range(n):
        onedim.append([])
    for point in points:
        slot = findSubdivision(onedim[0], point)    
        onedim[slot+1].append(point)
    return None

twodim = []
def buildTwoDim(points,n):
    del twodim[:] #erasing previous data

    #your code here

    return None

def pointInRectangle(point, bottomLeft, topRight):
    
    foundInside = False

    if point[0] >= bottomLeft[0] and point[1] >= bottomLeft[1]:
        if point[0] <= topRight[0] and point[1] <= topRight[1]:
            foundInside = True
    #print "pointInRectangle:"
    #print "point", point
    #print "bottomLeft", bottomLeft
    #print "topRight", topRight
    #print "foundInside?: ", foundInside
    return foundInside

def queryNaive(x0, y0, x1, y1):
    count = 0
    #your code here
    for point in naive:
        count += pointInRectangle(point, (x0, y0), (x1, y1))
    print "qn: ", count
    return count

    

def queryOneDim(x0, y0, x1, y1):
    count = 0

    #your code here
    leftWall = findLeftWall(onedim[0], (x0, y0))
    rightWall = findRightWall(onedim[0], (x1, y1))
    for region in onedim[1:]:
        for point in region:
            if pointInRectangle(point, (x0, y0), (x1, y1)):
                count += 1
    print "Left: %d %f\nRight: %d %f" %(leftWall, onedim[0][leftWall], rightWall, onedim[0][rightWall])
    return count

def queryTwoDim(x0, y0, x1, y1):
    count = 0

    #your code here

    return count
