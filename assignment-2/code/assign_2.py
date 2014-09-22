import sys

def initialize_db():
  fieldNames = 'Job ID,Agency,# Of Positions,Business Title,Civil Service Title,Salary Range From,Salary Range To,Salary Frequency,Work Location,Division/Work Unit,Job Description,Minimum Qual Requirements,Preferred Skills,Additional Information,Posting Date'
  fieldNames = fieldNames.split(',')
  db = {'Jobs': [], 'Agencies': {}]

  # initialize Table 1
  db['Jobs'] = fieldNames
  db['Jobs'][1] = ['Agency ID']

  # initialize Table 2
  db['Agencies'] = ['Agency ID', 'Agency']

  return db
  
  # schema:
  
  #print fieldNames

##def writeTable(table):
##  for column in table:
##    outString = ''
##    for row in column:
##      outString = outString + row
##      
##
##def save_db(db, file = "databaseasdf.txt"):
##  print "savedb"
##  with open(file, 'w') as f:
##    f.write("Table 1: Jobs")
##    writeTable(f, db['jobs'])
##    writeTable(f, db['agencies'])
##    writeTable(f, db['salary'])



def clear():
  # TODO Complete with your code and remove print below.
  print 'clear'    


# Inserts a job offer into the database.
def insert(db, fieldValues):
  # TODO Complete with your code and remove print below.
  
  #print 'insert ' + str(fieldValues)
  agencyName = fieldValues[1]
  if agencyName in db['Agencies']['nameToID']:
    agencyID = db['Agencies']['nameToID'][agencyName]
  else:
    agencyID = max(db['Agencies']['IDtoName'].keys()) + 1
    db['Agencies']['nameToID'][agencyName] = agencyID
    db['Agencies']['IDtoName'][agencyID] = agencyName

# Updates all job offers that attend the field_name=old_value pair.
def update_all(db, params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]

    # TODO Complete with your code and remove print below.
    print 'update_all set ' + update_field_name + '=' + update_field_value\
    + ' where ' + query_field_name + '=' + query_field_value

    # Prints number of updated rows in the database.
    updatedRowCount = 0
    print str(updatedRowCount)


# Deletes all job offers that attend the field_name=field_value pair.
def delete_all(db, params):
  field_name, field_value = params
  
  # TODO Complete with your code and remove print below.
  print 'delete_all where ' + field_name + '=' + field_value


# Prints all job offers that match the query field_name=field_value, one per
# line, semicolon-separated, with fields in the order defined in the assignment.
def find(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  print 'find where ' + field_name + '=' + field_value


# Prints how many job offers match the query field_name=field_value.
def count(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  print 'count job offers where ' + field_name + '=' + field_value


# Prints all job offers in the database, one per line, semicolon-separated, with
# fields in the order defined in the assignment.
def dump(params):
  # TODO Complete with your code and remove print below.
  print 'dump'


# Prints all job offers, one per line, semicolon-separated, but only the
# specified fields, in the order specified for the view.
def view(fieldNames):
  # TODO Complete with your code and remove print below.
  print 'view for fields ' + str(fieldNames)


def executeCommand(db, commandLine):
  tokens = commandLine.split('|') #assume that this symbol is not part of the data
  command = tokens[0]
  parameters = tokens[1:]

  if command == 'insert':
    insert(db, parameters)
  elif command == 'delete_all':
    delete_all(parameters)
  elif command == 'update_all':
    update_all(parameters)
  elif command == 'find':
    find(parameters)
  elif command == 'count':
    count(parameters)
  elif command == 'count_unique':
    count_unique(parameters)
  elif command == 'clear':
    clear()
  elif command == 'dump':
    dump(parameters)
  elif command == 'view':
    view(parameters)
  else:
    print 'ERROR: Command %s does not exist' % (command,)
    assert(False)

def executeCommands(db, commandFileName):
  f = open(commandFileName)
  for line in f:
    executeCommand(db, line.strip())

if __name__ == '__main__':
  #TODO: You should load the data from the database here
  print 'load'
  db = initialize_db()
  #
  path = "/Users/petervarshavsky/Documents/Git_NYU/Principles-of-informatics/Pr-informatics/assignment-2/data/"
  file1 = path + "sample_data_problem_1.txt"
  executeCommands(db, file1)
  #executeCommands(sys.argv[1])
  #TODO: You should save the data here
  print 'save'
