import sys
import time
import csv

import scipy.spatial as sps
import matplotlib.pyplot as plt
def loadRoadNetworkIntersections(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    listWithIntersectionCoordinates = []
    f = open(filename)
    reader = csv.reader(f, delimiter=' ')
    for l in reader:
        try:
            point = [float(l[0]),float(l[1])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                listWithIntersectionCoordinates.append(point)
        except:
            print l

    return listWithIntersectionCoordinates

def loadTaxiTrips(filename):
    #load pickup positions
    loadPickup = True
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    if loadPickup:        
        lngIndex = header.index(' pickup_longitude')
        latIndex = header.index(' pickup_latitude')
    else:
        latIndex = header.index(' dropoff_latitude')
        lngIndex = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point = [float(l[latIndex]),float(l[lngIndex])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                result.append(point)

        except:
            print l
    return result
   
def distSquare(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 
 
def naiveApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them

    for tripPickup in tripLocations:
        #tripPickup = tuple(tripPickup)
        for intInd, intersection in enumerate(intersections):
            newDistance = distSquare(intersection, tripPickup)
            if newDistance <= distanceThreshold:
                if intInd in counts:
                    counts[intInd] += 1
                else:
                    counts[intInd] = 1

    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return counts

def kdtreeApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()


    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip
    counter = 0
    tree = sps.KDTree(intersections)
    for tripPickup in tripLocations:
        points = tree.query_ball_point(tripPickup, r = distanceThreshold)
        for point in points:
            if point in counts:
                counts[point] += 1
            else:
                counts[point] = 1

        #for i in range(len(points)):
        #    intersection = tuple(intersections[points[i]])
        #    if intersection in counts:
        #        counts[intersection] += 1
        #    else:
        #        counts[intersection] = 1
    

    #
    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return counts

def plotResults(intersections, counts):
    #TODO: intersect the code to plot here
    lats, longs = zip(*intersections)
    
    sizes = []
    
    for intInd, intersect in enumerate(intersections):
        try:
            sizes.append(counts[intInd])
        except KeyError:
            sizes.append(0)
    
    sizes = [size*2 for size in sizes]
    
    fig, ax = plt.subplots()
    ax.scatter(longs, lats, marker = '.', lw = 0, color = "dodgerblue", alpha = 0.6, s= sizes)
    plt.show()    

def extraCredit(intersections, counts):
    #TODO: intersect the code to plot here
    print 'DONE'

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
    tripPickups       = loadTaxiTrips(sys.argv[2])
    distanceThreshold = float(sys.argv[3])

    #You need to implement this one. You need to make sure that the counts are correct
    naiveCounts = naiveApproach(roadIntersections,tripPickups, distanceThreshold)

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups, distanceThreshold)

    #
    plotResults(roadIntersections,kdtreeCounts)
