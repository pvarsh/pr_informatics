# Functions for students to implement.
def solveOnlyLists(inputList):
    uniqueList = []
    #compute unique items in inputList
    for x in inputList:
        if x not in uniqueList:
            uniqueList.append(x)
    return uniqueList

def solveDict(inputList):
    #compute unique items in inputList
    uniqueDict = {x:None for x in inputList}
    
    return uniqueDict.keys()

def solveSorted(sortedInputList):
    #compute unique items in inputList
    if len(sortedInputList) == 0:
        uniqueList = []    
    else:
        uniqueList = [sortedInputList[0]]
        for x in sortedInputList:
            if x != uniqueList[-1]:
                uniqueList.append(x)
    return uniqueList
