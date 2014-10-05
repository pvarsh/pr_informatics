import numpy as np
import problem3 as p3
import matplotlib.pyplot as plt

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
print "%d points: " %len(points), points

## naive:
p3.buildNaive(points, n)


p3.onedim = [1,2,3]
p3.buildOneDim(points, n)
#print "after creating is done: ", p3.onedim 
prettyPrintOneDim(p3.onedim)

bottomLeft = (.5, .4)
topRight = (.9,.9)
print "####### counting oneDim ########"
countOneDim = p3.queryOneDim(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])
print "####### counting naive  ########"
countNaive = p3.queryNaive(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])
print "countOneDim: ", countOneDim
print "countNaive:  ", countNaive

print "####### building twodim ########"
p3.buildTwoDim(points, n)
print p3.twodim

print "####### query twodim ########"
countTwoDim = p3.queryTwoDim(bottomLeft[0], bottomLeft[1], topRight[0], topRight[1])
print "countTwoDim: ", countTwoDim

### plotting
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

