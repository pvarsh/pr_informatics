import math

# Functions for students to implement.

naive = []
def buildNaive(points,n):
    ## Copies a list of points passed as an argument into the global (module) variable
    del naive[:] #erasing previous data

    #your code here
    for point in points:
        naive.append(point)
    return None

def makeWallsOneDim(n):
    ## Makes n + 1 vertical subdivision walls,
    ## where the first wall is 0.0 and last is 1.0
 
    subDiv = [0 + round(float(k)/n, 7) for k in range(n)]
    subDiv.append(1.0)
    return subDiv

#def findSubdivision(subDivision, point):
#    ## Replaced with findLeftWall
#    wall = 0
#    while subDivision[wall] <= point[0] and subDivision[wall] != 1.0:
#        wall += 1
#    wall = wall - 1
#    return wall

#def findLeftWall(subDivision, point):
#    ## Given a point finds the rightmost wall to the left of the point
#    ## Used by buildOneDim(), queryOneDim()
#    ## Stupid method using linear search
#
#    wall = 0
#    while subDivision[wall] <= point[0] and subDivision[wall] != 1.0:
#        wall += 1
#    wall = wall - 1
#    return wall

def findLeftWall(subDivision, point):
    delta = subDivision[1] - subDivision[0]
    #print "x coord: ", point[0]
    if point[0] == 1:
        leftWall = len(subDivision) - 2
    else:
        leftWall = int(math.floor(float(point[0]) / delta))
        #print "mathfloorleftwall: ", leftWall
    return leftWall

#def findRightWall(subDivision, point):
#    ## Given a point finds the rightmost wall to the left of the point
#    ## Used by queryOneDim()
#    ## Redundant! Doh!
#    wall = len(subDivision) - 2
#    while subDivision[wall] > point[0] and subDivision[wall] != 0:
#        wall -= 1
#    return wall

onedim = []

def buildOneDim(points,n):
    ## builds onedim structure
    ## onedim[0] is the list of walls
    ## onedime[1:] are the lists of points from points that fall into corresponding regions

    del onedim[:] #erasing previous data

    #your code here
    onedim.append(makeWallsOneDim(n))
    for k in range(n):
        onedim.append([])
    for point in points:
        slot = findLeftWall(onedim[0], point)    
        onedim[slot+1].append(point)
    return None

twodim = []
def buildTwoDim(points,n):
    del twodim[:] #erasing previous data

    #your code here

    return None

def pointInRectangle(point, bottomLeft, topRight):
    ## checks if given point is in the rectangle described by bottomLeft and topRight
    ## used by queryNaive(), queryOneDim() 
    
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
    ## counts the number of points in rectangle described by (x0, y0) and (x1, y1)
    ## uses global variable 'naive'
    
    count = 0
    #your code here
    for point in naive:
        count += pointInRectangle(point, (x0, y0), (x1, y1))
    #print "qn: ", count
    return count

    

def queryOneDim(x0, y0, x1, y1):
    ## counts the number of points in rectangle described by (x0, y0) and (x1, y1)
    ## uses global variable 'onedim'

    count = 0

    #your code here
    leftWall = findLeftWall(onedim[0], (x0, y0))
    rightWall = findLeftWall(onedim[0], (x1, y1)) # was findRightWall(...)
    for region in onedim[1+leftWall:rightWall]:
        for point in region:
            if pointInRectangle(point, (x0, y0), (x1, y1)):
                count += 1
    #print "Left: %d %f\nRight: %d %f" %(leftWall, onedim[0][leftWall], rightWall, onedim[0][rightWall])
    return count

def queryTwoDim(x0, y0, x1, y1):
    count = 0

    #your code here

    return count
