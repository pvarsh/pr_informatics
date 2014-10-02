from collections import *
import sys
import random
import time
import math
from problem2 import *

#Test if plot modules are available
import imp
try:
  import matplotlib.pyplot as plt
  import numpy as np
  foundPlotModules = True
except ImportError:
  foundPlotModules = False



# Returns a list with n random integers, sorted or not.
def generateList(n, isSorted):
  L = [random.randint(0,100) for i in range(n)]
  return sorted(L) if isSorted else L



# Tests the search solution for a given function solFunc, using input lists of
# given sizes, sorted or not. Returns average time that solution took for each
# different list size.
def testSolutionVInL(solFunc, sizes, isSorted):
  numRepetitions = 10
  solutionTimes = {}
  # For each n
  for n in sizes:
    # Runs solution multiple times to store the time to solve.
    timesForN = []
    for repIndex in xrange(numRepetitions):
      # Generates random input.
      L = generateList(n, isSorted)
      v = random.randint(0, 100)

      # Computes solution and stores time to solve for this n.
      startTime = time.time()
      solFunc(L, v)
      ellapsedTime  = time.time() - startTime
      timesForN.append(ellapsedTime)
    
    # Computes and stores average time for this n.
    solutionTimes[n] = sum(timesForN) / numRepetitions

  return solutionTimes



# Tests the range search solution for a given function solFunc, using input
# lists of given sizes, sorted or not. Returns average time that solution took
# for each different list size.
def testSolutionRange(solFunc, sizes, isSorted):
  numRepetitions = 10
  solutionTimes = {}
  # For each n
  for n in sizes:
    # Runs solution multiple times to store the time to solve.
    timesForN = []
    for repIndex in xrange(numRepetitions):
      # Generates random input.
      L = generateList(n, isSorted)
      v1 = 1
      v2 = 0
      while v1 > v2:
        v1 = random.randint(0, 100)
        v2 = random.randint(0, 100)

      # Computes solution and stores time to solve for this n.
      startTime = time.time()
      solFunc(L, v1, v2)
      ellapsedTime  = time.time() - startTime
      timesForN.append(ellapsedTime)
    
    # Computes and stores average time for this n.
    solutionTimes[n] = sum(timesForN) / numRepetitions

  return solutionTimes



# Builds plots.
def buildPlot(plotsData, useLogScale, maxSize):
  colors = ['blue','green','red','magenta','cyan']

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)

  index = 0
  for func, plot in plotsData.iteritems():
    mylabel = str(func).split(' ')[1]
    xlist = [t[0] for t in plot]
    ylist = [t[1] for t in plot]
    x  = np.array(xlist)
    y  = np.array(ylist)
    xerr = 0
    yerr = 0
    ls = 'dotted'
    mycolor = colors[index % len(colors)]
    plt.errorbar(x, y, xerr=xerr, yerr=yerr, ls=ls, color=mycolor,label=mylabel,linewidth=2.0)
    index += 1

  ax.set_xlim((-1, 7 if useLogScale else maxSize))
  ax.set_title('Performance Evaluation')  
  plt.xlabel('Input List Size (logscale)')  
  plt.ylabel('Avg Running Time (seconds)')  
  plt.legend(loc = 2)
  plt.show()



# Prepares data to use in plot.
def getPlotData(solutionData, sizes, useLogScale):
  # Converts data to use in plot.
  plotData = []
  for size in sizes:
    x = math.log(size, 10) if useLogScale else size
    plotData.append((x, solutionData[size]))
  return plotData



#Test script
if __name__ == '__main__':
  useLogScale = True

  sizes = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000]

  functionsToTestVInL = [\
  searchGreaterNotSorted, searchGreaterSorted, searchGreaterBinSearch]

  sortedToTestVInL = [False, True, True]

  # Runs functions that test whether v is in L (sorted or not).
  plots = OrderedDict()
  for i, func in enumerate(functionsToTestVInL):
    print 'Testing ', func.__name__
    isSorted = sortedToTestVInL[i]
    solutionData = testSolutionVInL(func, sizes, isSorted)
    # Converts data to use in plot.
    plots[func] = getPlotData(solutionData, sizes, useLogScale)

  # Runs range search.
  print 'Testing ', searchInRange.__name__
  isSorted = True
  solutionData = testSolutionRange(searchInRange, sizes, isSorted)
  # Converts data to use in plot.
  plots[searchInRange] = getPlotData(solutionData, sizes, useLogScale)

  # Finally plots timing results.
  if foundPlotModules:
    buildPlot(plots, useLogScale, sizes[-1])
  else:
    print plots

