# download assignment 2 data files using
# http://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python

import urllib

# download sample data files
fileNamePrefix = "sample_data_problem_"

filePath = "http://vgc.poly.edu/projects/gx5003-fall2014/week2/lab/data/"
inputFilePrefix = "sample_data_problem_"
outputFilePrefix = "sample_output_problem_"

testURL = "http://vgc.poly.edu/projects/gx5003-fall2014/week2/lab/data/sample_data_problem_1.txt"
csvURL = "http://vgc.poly.edu/projects/gx5003-fall2014/week2/lab/data/NYC_Jobs_sample.csv"

csvfile = urllib.URLopener()
csvfile.retrieve(csvURL, "NYC_Jobs_sample.csv")

for x in range(1, 7):
    inputFileName = inputFilePrefix + str(x) + ".txt"
    inputFileURL = filePath + inputFileName

    outputFileName = outputFilePrefix + str(x) + ".txt"
    outputFileURL = filePath + outputFileName
 
    testfile = urllib.URLopener()
    testfile.retrieve(inputFileURL, inputFileName)
    testfile = urllib.URLopener()
    testfile.retrieve(outputFileURL, outputFileName)
