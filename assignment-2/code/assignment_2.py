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
                
            

def clear(db):
    for i, column in enumerate(db):
        print column
        print column[0]
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
            values[n] = int(n)
        for n in whichFloat:
            values[n] = float(n)
    
    command = command[0]
    return command, values

def insert(db, valueList):
    print db
    for i, value in enumerate(valueList):
        db[i].append(value)

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
    print "\nNumber of columns: ", len(db)
    print db
    clear(db)
    print db
 

    #readCommandFile(db, file)
    
    
#[[id], [numPos], [busTitle], [civServTitle]]

path = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/assignment-2/data/"
file1 = path + "sample_data_problem_1.txt"
csvFile = path + "NYC_Jobs_sample.csv"
#readCommands(file1)
#print readHeader(csvFile)
test(csvFile, file1)
