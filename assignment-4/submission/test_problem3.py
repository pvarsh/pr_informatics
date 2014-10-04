import sys
import random
import time
import math

from problem3 import *

#Test if plot modules are available
import imp
try:
    import matplotlib.pyplot as plt
    import numpy as np
    foundPlotModules = True
except ImportError:
    foundPlotModules = False


def generateSampleInput(inputSize):
    sampleInput = []
    for i in xrange(inputSize):
        sampleInput.append((random.random(), random.random()))

    return sampleInput

def testSolution(buildFunc, queryFunc, sizes,n):
    numRepetitions = 20
    solutionTimes = {}
    for inputSize in sizes:
        solutionTimes[inputSize] = []
        sampleInput = generateSampleInput(inputSize)
        buildFunc(sampleInput,n)
        for repIndex in xrange(numRepetitions):
            x0 = random.uniform(0,1)
            y0 = random.uniform(0,1)
            x1 = random.uniform(x0,1)
            y1 = random.uniform(y0,1)
            startTime = time.time()
            queryFunc(x0,y0,x1,y1)
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


def buildPlot(n, plots):
    colors = ['blue','green','red','magenta','cyan']

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    index = 0
    for i in plots:
        func = i[0]
        plot = i[1]
        mylabel = str(func[1]).split(' ')[1]
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

    ax.set_xlim((-1, 1000000))
    ax.set_title('Performance Evaluation with n='+str(n))    
    plt.xlabel('Input List Size')    
    plt.ylabel('Avg Running Time (seconds)')    
    plt.legend(loc=2)
    plt.show()


#Test script
if __name__ == '__main__':
    sizes = [1000,10000,50000,100000,500000,1000000]
    ns    = [1000]
    functionsToTest = [(buildNaive, queryNaive), (buildOneDim, queryOneDim), (buildTwoDim, queryTwoDim)]

    for n in ns:
        plots = []
        for func in functionsToTest:
            print 'Testing', func[0], func[1]
            solutionTimes = testSolution(func[0],func[1],sizes,n)
            plotData = computePlotData(solutionTimes)        
            logScalePlotData = []
            for size in sizes:
                #logScalePlotData.append((math.log(size,10),plotData[size]))
                logScalePlotData.append((size,plotData[size]))
            plots.append((func,logScalePlotData))
        if foundPlotModules:
            buildPlot(n, plots)
            #print plots
        else:
            print plots

