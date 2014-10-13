#### Test cases for assignment 4 problem 3
#### Author: Peter Varshavsky
####
#### Generates:
####    - p random points
####    - random box to search in
####    - grid of n vertical slots for onedim
####    - grid of nxn slots for twodim
#### Runs naive, onedim, and twodim functions to build and count points in the random box
#### Prints out search results and plots the box and points
#### 
#### To use:
####    place in the same directory as your problem3.py file
####    in terminal run  
####    $ python ssign4_p3_random_test.py
####
#### Note:
####    the data structures naive, onedim, and twodim are globals in the namespace of your module problem3

import random
import numpy as np
import problem3 as p3
import matplotlib.pyplot as plt


### plotting
def plotExample(points, bottomLeft, topRight):
    xpoints = [point[0] for point in points]
    ypoints = [point[1] for point in points]
    plt.plot(xpoints, ypoints, 'co')
    for wall in p3.onedim[0]:
        plt.axhline(y = wall, color = "#aaaaaa", linestyle = '--')
        plt.axvline(x = wall, color = "#aaaaaa", linestyle = '--')
    boxColor = "#ee9a00"
    plt.axhline(y = bottomLeft[1], xmin = bottomLeft[0], xmax = topRight[0], color = boxColor)
    plt.axhline(y = topRight[1], xmin = bottomLeft[0], xmax = topRight[0], color = boxColor)
    plt.axvline(x = bottomLeft[0], ymin = bottomLeft[1], ymax = topRight[1], color = boxColor)
    plt.axvline(x = topRight[0], ymin = bottomLeft[1], ymax = topRight[1], color = boxColor)
    plt.show()

##### random box
bottomLeft = [1,1] # these numbers don't matter, just initialization
topRight = [1,1] # these numbers don't matter, just initialization
bottomLeft[0], topRight[0] = tuple(sorted([random.uniform(0,1) for x in range(2)]))
bottomLeft[1], topRight[1] = tuple(sorted([random.uniform(0,1) for x in range(2)]))

##### setting number of subdivisions and points
n = 20 # subdivisions
p = 40 # number of points

##### generating p random points
points = [(random.uniform(0,1), random.uniform(0,1)) for x in range(p)]

##### building data structures (using your functions in problem3.py)
p3.buildNaive(points, n)
p3.buildOneDim(points, n)
p3.buildTwoDim(points, n)

##### printing counts by three methods (using your functions in problem3.py)
print "Naive count: ", p3.queryNaive(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])
print "OneDim count: ", p3.queryOneDim(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])
print "TwoDim count: ", p3.queryTwoDim(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])

##### plotting all of the above
plotExample(points, bottomLeft, topRight)
