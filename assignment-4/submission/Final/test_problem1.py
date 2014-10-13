from problem1 import *
import sys
import random
import time
import math
from collections import *

#Test if plot modules are available
import imp
try:
    import matplotlib.pyplot as plt
    import numpy as np
    foundPlotModules = True
except ImportError:
    foundPlotModules = False


def solveWithSet(inputList):
    outputSet = set(inputList)
    return list(outputSet)


def generateSampleInput(inputSize,isSorted=False):
    sampleInput = []
    for i in xrange(inputSize):
        sampleInput.append(random.randint(0,100))
    if isSorted:
        sampleInput.sort()
    return sampleInput


def testSolution(solFunc,sizes):
    numRepetitions = 10
    solutionTimes = {}
    isSorted = (solFunc == solveSorted)
    for inputSize in sizes:
        solutionTimes[inputSize] = []
        for repIndex in xrange(numRepetitions):
            sampleInput = generateSampleInput(inputSize,isSorted)
            startTime = time.time()
            solFunc(sampleInput)
            ellapsedTime  = time.time() - startTime
            solutionTimes[inputSize].append(ellapsedTime)

    return solutionTimes


def computePlotData(solutionTimes):
    plotData = {}
    for solutionSize in solutionTimes:
        repetitionTimes = solutionTimes[solutionSize]
        avgTime = sum(repetitionTimes)/len(repetitionTimes)
        plotData[solutionSize] = avgTime
    return plotData


def buildPlot(plots):
    colors = ['blue','green','red','magenta','cyan']

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    index = 0
    for func, plot in plots.iteritems():
        mylabel = str(func).split(' ')[1]
        xlist = [t[0] for t in plot]
        ylist = [t[1] for t in plot]
        x    = np.array(xlist)
        y    = np.array(ylist)
        xerr = 0
        yerr = 0
        ls = 'dotted'
        mycolor = colors[index % len(colors)]
        plt.errorbar(x, y, xerr=xerr, yerr=yerr, ls=ls, color=mycolor,label=mylabel,linewidth=2.0)
        #
        index += 1

    ax.set_xlim((-1, 7))
    ax.set_title('Performance Evaluation')    
    plt.xlabel('Input List Size (logscale)')    
    plt.ylabel('Avg Running Time (seconds)')    
    plt.legend(loc=2)
    plt.show()


#Test script
if __name__ == '__main__':
    sizes = [10,100,1000,10000,50000,100000,500000,1000000]
    functionsToTest = [solveOnlyLists, solveDict,solveSorted,solveWithSet]
    plots = OrderedDict()
    for func in functionsToTest:
        print 'Testing', func
        solutionTimes = testSolution(func,sizes)
        plotData = computePlotData(solutionTimes)        
        logScalePlotData = []
        for size in sizes:
            logScalePlotData.append((math.log(size,10),plotData[size]))
        plots[func] = logScalePlotData
    if foundPlotModules:
        buildPlot(plots)
    else:
        print plots
