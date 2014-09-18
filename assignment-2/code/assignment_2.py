#################################
# Principles of Urban Informatics
# Assignment 2
# Peter Varshavsky
#################################

import csv

def readHeader(filename):
    # initializes a database as list of lists
    # with the first element of each sublist being the header element
    # from given header file
    
    with open(filename, 'r') as f:
        header = f.next()[:-2] # cutting off '\r\n' at end of line
        header = header.split('|')
        db = [[colName] for colName in header] # initialize the database
    return db

def readCommandFile(db, file):
    with open(file, 'r') as f:
        for line in f:
            command, values = readCommandLine(line)
            #print [v for v in values]
            if command == 'clear':
                clear(db)
            if command == 'insert':
                try:
                    insert(db, values)
                except Exception as detail:
                    print "Exception: ", detail
            if command == 'dump':
                print 'output file name?'
            if command == 'update_all':
                try:
                    update_all(db, values)
                except ValueError as detail:
                    print "Insert warning: ", detail
            if command == 'delete_all':
                delete_all(db, values)
                
            
def clear(db):
    # clears the database
    # keeps column names
    for i, column in enumerate(db):
        db[i] = [column[0]]

def readCommandLine(lineString):
    # reads a line from file of commands and parses it into
    # command and parameter values, returning the values as a list
    if lineString[-1] == '\n':
        lineString = lineString[:-1]
    #command = lineString.split('|')
    command = csv.reader([lineString], delimiter = '|', quotechar = '"').next()
    values = command[1:]

    # converting id, number of open positions and salary fields to numeric
    #if len(values) == 15:
    #    whichInt = [0, 2] #these indeces to be converted to integer
    #    whichFloat = [5, 6] #these indeces to be converted to float

    #    for n in whichInt:
    #        values[n] = int(values[n])
    #    for n in whichFloat:
    #        values[n] = float(values[n])

    command = command[0]
    return command, values

def insert(db, valueList):
    # insert values into database if job_id is not already in the database

    if len(valueList) != 15:
        print len(valueList)
        raise Exception("Invalid number of parameters. Must have 15")
    print "Length of value list: ", len(valueList)
    print "Job ID: ", valueList[0]
    if valueList[0] not in db[0]:
        for i, value in enumerate(valueList):
            db[i].append(value)
    else:
        print "Duplicate id. Not included"

def dump(db):
    pass
    
def createCommandsDict():
    # creates a dictionary of commands
    pass

def readCommands(filename):
    # currently not used
    with open(filename, 'r') as f:
        for line in f:
            print line[0:20]

def update_all(db, values):
    # make list of column names
    #       values[0] is query_field_name
    #       values[1] is query_field_value
    #       values[2] is update_field_name
    #       values[3] is update_field_value

    
    qf_index = getCol(db, values[0]) # query field index
    uf_index = getCol(db, values[2]) # update field index

    # converting strings to numbers for id, salary range, # positions open
    #if qf_index in [0, 2]:
    #    print "AAA qf_index: ", qf_index
    #    values[1] = int(values[1])
    #if qf_index in [5, 6]:
    #    values[1] = float(values[1])
    #if uf_index in [0, 2]:
    #    values[3] = int(values[3])
    #if uf_index in [5, 6]:
    #    values[3] = float(values[3])

##    update_rows = [i for i, x in enumerate(db[qf_index]) if x == values[1]]
##    if len(update_rows) == 0:
##        raise ValueError("Query field value does not exist in the database")
    update_rows = getRows(db, qf_index, values[1])
    
    print "Update where column ", qf_index, " has value ", values[1]
    print "Rows to be updated: ", update_rows

    for row in update_rows:
        db[uf_index][row] = values[3]

def getRows(db, qf_index, query_value):
    return [i for i, x in enumerate(db[qf_index]) if x == query_value]

def getCol(db, name):
    # returns index of query field column
    
    colNames = [col[0] for col in db]
    try:
        qf_index = colNames.index(name)
    except ValueError:
        raise ValueError("Query field name does not exist in database")
    return qf_index

def delete_all(db, values):
    print "Before deletion: "
    prettyPrint(db)
    print "delete_all: query_field_name = ", values[0]
    try:
        qf_index = getCol(db, values[0])
        delete_rows = getRows(db, qf_index, values[1])
        print "QF_Name: ", [values[0]], " QF_Value: ", [values[1]]
        print delete_rows
        delete_rows.sort(reverse = True)
        print "Rows to be deleted: ", delete_rows
        print "After deletion: "
        prettyPrint(db)
    except ValueError as detail:
        print "Warning: ", detail

    
    

def test(csvFile, file):
    db = readHeader(csvFile)
    clear(db)
 
    readCommandFile(db, file)
    prettyPrint(db)

    return db

def prettyPrint(db, maxrows = 200, nchar = 10):
    # prints the database in fixed width column format
    nrows = min(len(db[0]), maxrows)

    outstring = ''
    for row in xrange(nrows):
        for column in db:
            outstring = outstring + ' | ' + str(column[row])[:nchar].ljust(nchar)
        outstring = outstring + '\n'
    print outstring
        
def makeTestCase1(fileOut, nrows = 5):

    strOut = 'clear\n'
    for row in range(nrows):
        strOut = strOut + 'insert'
        strOut = strOut + '|' + str(row) + str(row)
        for col in range(1,15):
            if col in [2, 5, 6]:
                strOut = strOut + '|' + '33'
            else: 
                strOut = strOut + '|' + 'r' + str(row) + 'c' + str(col)
        strOut= strOut + '\n'
    print strOut

    with open(fileOut, 'w') as f:
        f.write(strOut)
    
            
        
    
#[[id], [numPos], [busTitle], [civServTitle]]



path = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/assignment-2/data/"
file1 = path + "sample_data_problem_1.txt"
file2 = path + "sample_data_problem_2.txt"
file3 = path + "sample_data_problem_3a.txt"
tc1 = path + "test_case_1.txt"
csvFile = path + "NYC_Jobs_sample.csv"

#makeTestCase1(tc1)

#readCommands(file1)
#print readHeader(csvFile)
db = test(csvFile, file3)


