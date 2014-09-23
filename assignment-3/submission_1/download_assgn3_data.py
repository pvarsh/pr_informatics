# download assignment 3 data files using
# http://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python

import urllib

# download sample data files

inputFileNameSuffix = [str(x) for x in range(1,9)] + ['3_1', '3_2']
#inputFileNameSuffix.remove('3')
inputFileNameSuffix.sort()
outputFileNameSuffix = [str(x) for x in range(1,9)]

filePath = "http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/"

inputFilePrefix = "sample_data_problem_"
outputFilePrefix = "sample_output_problem_"

for x in inputFileNameSuffix: 
    inputFileName = inputFilePrefix + x + ".txt"
    inputFileURL = filePath + inputFileName   
 
    outputFileName = outputFilePrefix + x + ".txt"
    outputFileURL = filePath + outputFileName
 
    try:
        testfile = urllib.URLopener()
        testfile.retrieve(inputFileURL, inputFileName)
        print inputFileURL
    except (RuntimeError, IOError):
        pass
    try:
        testfile = urllib.URLopener()
        testfile.retrieve(outputFileURL, outputFileName)
        print outputFileURL
    except (RuntimeError,IOError):
        pass 
