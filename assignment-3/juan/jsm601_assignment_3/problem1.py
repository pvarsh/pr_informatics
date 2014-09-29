import sys
import csv 
from datetime import datetime

def problem1(f):
	with open(f) as f:
		data =[r for r in csv.reader(f)]
	time_min = min([datetime.strptime(d[1], "%a %b %d %H:%M:%S %Z %Y") for d in data]).strftime("%B %d %Y, %H:%M:%S")
	time_max = max([datetime.strptime(d[1], "%a %b %d %H:%M:%S %Z %Y") for d in data]).strftime("%B %d %Y, %H:%M:%S")
	
	print "There were %s" %len(data) +" tweets between " + time_min + " and " + time_max

problem1(sys.argv[1])
