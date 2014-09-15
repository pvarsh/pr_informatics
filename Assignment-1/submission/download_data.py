# download data files using
# http://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python

import urllib

# download sample data files
path = "http://vgc.poly.edu/projects/gx5003-fall2014/week1/lab/data/"
fileNamePrefix = "sample_data_problem_"

for x in range(1, 9):
    fileName = fileNamePrefix + str(x) + ".csv"
    fileURL = path + fileName

    testfile = urllib.URLopener()
    testfile.retrieve(fileURL, fileName)

# download neighborhood zip code table
fileName = "zip_borough.csv"
fileURL = path + fileName

testfile = urllib.URLopener()
testfile.retrieve(fileURL, fileName)

