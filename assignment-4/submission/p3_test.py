import numpy as np
import problem3 as p3

def prettyPrintOneDim(oneDim):
    print "############# onedim ##############"
    print "Walls: ", oneDim[0]
    for region in oneDim[1:]:
        print region 
    print "############# /onedim ##############"


##### nonrandom test with 4 subdivisions

n = 4
points = [((0.5 + k)/n, 0.5) for k in range(n)]
points.append((1, 0.5))
points.append((0, 0.5))
points.append((0.5, 0.5))
points.append((0.999, 0.5))
points.sort()
print "Points: ", points

## naive:
p3.buildNaive(points, n)


p3.onedim = [1,2,3]
p3.buildOneDim(points, n)
#print "after creating is done: ", p3.onedim 
prettyPrintOneDim(p3.onedim)

bottomLeft = (.5, 0)
topRight = (5,1)
print "####### counting oneDim ########"
countOneDim = p3.queryOneDim(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])
print "####### counting naive  ########"
countNaive = p3.queryNaive(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])
print "countOneDim: ", countOneDim
print "countNaive:  ", countNaive
