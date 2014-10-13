import ConfigParser
import sys, os
import MySQLdb


# Some nasty globals.
PROBLEM_COUNT = 6
MUST_SORT = {i+1: True for i in range(PROBLEM_COUNT)}
MUST_SORT[3] = False

FIELDS = {}
FIELDS[1] = ["count(*)"]
FIELDS[2] = ["name"]
FIELDS[3] = ["lat", "lng", "ff"]
FIELDS[4] = ["name", "diff_feb1_jan18"]
FIELDS[5] = ["name", "diff_7d", "diff_30d"]
FIELDS[6] = ["stop_f"]



# Returns MySQL cursor.
def createCursor():
  dbConfig = ConfigParser.RawConfigParser()
  dbConfig.read("db.conf")
  user = dbConfig.get("database", "user")
  passwd = dbConfig.get("database", "passwd")
  database = dbConfig.get("database", "database")
  host = dbConfig.get("database", "host")
  db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
  return db.cursor()



# Runs a query and returns lines of returned values.
def runQuery(cursor, query, problem, mustSort):
  comments = ""
  result = []

  # Gets rows and field names.
  cursor.execute(query)
  field_names = {d[0]: i for i, d in enumerate(cursor.description)}

  # Validates columns.
  if len(field_names.keys()) != len(FIELDS[problem]):
      print "Double check the name of the columns for problem %d" % problem
      print "They should be " + str(FIELDS[problem])
      return
    
  for field in FIELDS[problem]:
    if not field in field_names:
      print "Double check the name of the columns for problem %d." % problem
      print "They should be " + str(FIELDS[problem])
      return

  rows = cursor.fetchall()

  for row in rows:
    cols = [str(row[field_names[col]]) for col in FIELDS[problem]]

    line = "(" + ",".join(cols) + ")"
    result.append(line)
  return sorted(result) if mustSort else result



# Runs a problem and returns lines of returned values.
def runProblem(cursor, problem, mustSort):
  filename = "query" + str(problem) + ".sql"
  query = ""
  with open(filename) as f:
    query = f.read()

  return runQuery(cursor, query, problem, mustSort)



# Creates expected result for a given problem.
def createExpectedResult(cursor, problem, mustSort):
  filename = "query_solution" + str(problem) + ".sql"
  query = ""
  with open(filename) as f:
    query = f.read()

  output_filename = "gt" + str(problem) + ".txt"
  with open(output_filename, "w") as f:
    result = runQuery(cursor, query, problem, mustSort)
    for row in result:
      f.write(row + "\n")



# Returns expected result for a given problem.
def getExpectedResult(cursor, problem, mustSort):
  filename = "gt" + str(problem) + ".txt"
  # Creates ground truth if it does not exist.
  if not os.path.isfile(filename):
    createExpectedResult(cursor, problem, mustSort)

  # Reads expected result and returns.
  with open(filename) as f:
    # Removes final \n
    return [row[:-1] for row in f]



# Runs a problem, sorts the returned lines if necessary,
# and grades according to expected result.
def gradeProblem(cursor, problem, isVerbose, mustSort):
  filename = "query" + str(problem) + ".sql"
  if not os.path.isfile(filename):
    print "Your grade in problem %d is 0 (%s does not exist)\n" % \
    (problem, filename)
    return
  else:
    try:
      expectedResult = getExpectedResult(cursor, problem, mustSort)
      result = runProblem(cursor, problem, mustSort)

      isEqual = len(result) == len(expectedResult) and\
      all(result[i] == expectedResult[i] for i in range(len(result)))

      grade = 10 if isEqual else 0
      comments = "" if isEqual else "(wrong result)"
      print "Your grade in problem %d is %d %s" % \
      (problem, grade, comments)
      if isVerbose:
        print "Your output:"
        for row in result:
          print row
        if grade != 10:
          print "Expected:"
          for row in expectedResult:
            print row
    except Exception as e:
      print "Your grade in problem %d is 0 (error in SQL)" % problem



if __name__ == "__main__":
  # Default: not verbose, grades all problems.
  problems = range(PROBLEM_COUNT)
  isVerbose = False

  # Specified problem.
  if len(sys.argv) > 1:
    problems = [int(sys.argv[1]) - 1]
    isVerbose = True

  cursor = createCursor()
  for p in problems:
    gradeProblem(cursor, p + 1, isVerbose, MUST_SORT[p + 1])
