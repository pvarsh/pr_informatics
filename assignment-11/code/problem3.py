import sys
import time
import csv
import math
import numpy as np
import scipy.spatial as sps


def loadTaxiTripsPickupAndDropoffs(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    lngIndex0 = header.index(' pickup_longitude')
    latIndex0 = header.index(' pickup_latitude')
    latIndex1 = header.index(' dropoff_latitude')
    lngIndex1 = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point0 = [float(l[latIndex0]),float(l[lngIndex0])]
            point1 = [float(l[latIndex1]),float(l[lngIndex1])]
            if latBounds[0] <= point0[0] <= latBounds[1] and lngBounds[0] <= point0[1] <= lngBounds[1] and latBounds[0] <= point1[0] <= latBounds[1] and lngBounds[0] <= point1[1] <= lngBounds[1]:
                result.append([point0[0],point0[1],point1[0],point1[1]])
        except:
            print l
    return result
   
def pointInRectangle(point, rectangle):
    if point[0] > rectangle[0][0] and point[0] < rectangle[0][1]:
        if point[1] > rectangle[1][0] and point[1] < rectangle[1][1]:
            return True
    else:
        return False
 
def naiveApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    startTime = time.time()

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them
    
    for i, trip in enumerate(tripLocations):
        if trip[0] > startRectangle[0][0] and trip[0] < startRectangle[0][1]:
            if trip[1] > startRectangle[1][0] and trip[1] < startRectangle[1][1]:
                if trip[2] > endRectangle[0][0] and trip[2] < endRectangle[0][1]:
                    if trip[3] > endRectangle[1][0] and trip[3] < endRectangle[1][1]:
                        indices.append(i)
    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return indices

def euclidDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def circumscribeRectangle(rectangle):
    """
    Finds center of rectangle given described by lower left and upper right points
    [[x0, x1], [y0, y1]]
    """
    xCenter = sum(rectangle[0])/2
    yCenter = sum(rectangle[1])/2
    
    radius = euclidDistance([rectangle[0][0], rectangle[1][0]], [xCenter, yCenter])

    return {'center': (xCenter, yCenter), 'r':radius}


def kdtreeApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    startTime = time.time()

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip
    
    startCircle = circumscribeRectangle(startRectangle)
    #endCircle = circumscribeRectangle(endRectangle)

    tripLocations = np.array(tripLocations)  
    tripStarts = tripLocations[0: , 0:2]
    tripEnds = tripLocations[0: , 2: ]
   
    # possible to improve by querying the starts tree before building the ends tree to only
    # build the ends tree on the subset returned by first query
 
    treeStarts = sps.KDTree(tripStarts)
    
    startsSubset = treeStarts.query_ball_point(startCircle['center'], r = startCircle['r'])

    for ind in startsSubset:
        if pointInRectangle(tripStarts[ind], startRectangle):
            if pointInRectangle(tripEnds[ind], endRectangle):
                indices.append(ind)
    #
    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return indices

def extraCredit(tripLocations, startPolygon, endPolygon):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startPolygon region and end in the endPolygon region
    indices = []

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip

    return indices    

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    trips             = loadTaxiTripsPickupAndDropoffs(sys.argv[1])
    #
    startRectangle    = [[40.713590,40.721319],[-74.011116,-73.994722]] #[[minLat,maxLat],[minLng,maxLng]]
    endRectangle      = [[40.744532,40.748398],[-74.003005,-73.990881]] #[[minLat,maxLat],[minLng,maxLng]]

    #You need to implement this one. You need to make sure that the counts are correct
    naiveIndices = naiveApproach(trips,startRectangle, endRectangle)

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeIndices = kdtreeApproach(trips,startRectangle, endRectangle)
