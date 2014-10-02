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
    uniqueList = []
    #compute unique items in inputList
    uniqueList = [x for i, x in enumerate(sortedInputList) if x != sortedINputList[i - 1]]
    return uniqueList
