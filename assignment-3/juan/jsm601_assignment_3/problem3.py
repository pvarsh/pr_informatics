import sys
import csv

def problem3(file_1, file_2):
	print "\n".join(sorted(list(set([item for sublist in [[row[i] for i in range(4, len(row))] for row in csv.reader(open(file_1))] for item in sublist]) &\
		set([item for sublist in [[row[i] for i in range(4, len(row))] for row in csv.reader(open(file_2))] for item in sublist]))))

problem3(sys.argv[1], sys.argv[2])

