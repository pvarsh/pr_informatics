#################################
# Principles of Urban Informatics
# Assignment 2
# Peter Varshavsky
#################################

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
                insert(db, values)
            if command == 'dump':
                print 'output file name?'
                
            

def clear(db):
    for i, column in enumerate(db):
        db[i] = [column[0]]

def readCommandLine(lineString):
    if lineString[-1] == '\n':
        lineString = lineString[:-1]
    command = lineString.split('|')
    values = command[1:]

    # converting id, number of open positions and salary fields to numeric
    if len(values) == 15:
        whichInt = [0, 2] #these indeces to be converted to integer
        whichFloat = [5, 6] #these indeces to be converted to float

        for n in whichInt:
            values[n] = int(values[n])
        for n in whichFloat:
            values[n] = float(values[n])

    command = command[0]
    return command, values

def insert(db, valueList):
    # insert values into database if job_id is not already in the database
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
    with open(filename, 'r') as f:
        for line in f:
            print line[0:20]

def test(csvFile, file):
    db = readHeader(csvFile)
    clear(db)
 

    readCommandFile(db, file)
    prettyPrint(db)

def prettyPrint(db, maxrows = 200, nchar = 10):
    # prints the database in fixed width column format
    nrows = min(len(db[0]), maxrows)

    outstring = ''
    for row in xrange(nrows):
        for column in db:
            outstring = outstring + ' | ' + str(column[row])[:nchar].ljust(nchar)
        outstring = outstring + '\n'
    print outstring
        

            
        
    
#[[id], [numPos], [busTitle], [civServTitle]]

path = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/assignment-2/data/"
file1 = path + "sample_data_problem_1.txt"
csvFile = path + "NYC_Jobs_sample.csv"
#readCommands(file1)
#print readHeader(csvFile)
test(csvFile, file1)
