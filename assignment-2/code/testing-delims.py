

import csv
testdata = ['48| "one| two"| "2011/11/03"']
testdata = ['123234|Field1|Another field|"Field that | uses delimiters"|Last field']
testcsv = csv.reader(testdata, delimiter = '|', quotechar = '"')
print testcsv.next()

