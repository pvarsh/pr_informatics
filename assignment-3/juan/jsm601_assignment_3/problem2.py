import sys
import csv 
from datetime import datetime

def problem2(file_1):
	with open(file_1) as f:
		data =[r for r in csv.reader(f)]
	users = set(u[0] for u in data)
	time_min = min([datetime.strptime(d[1], "%a %b %d %H:%M:%S %Z %Y") for d in data]).strftime("%B %d %Y, %H:%M:%S")
	time_max = max([datetime.strptime(d[1], "%a %b %d %H:%M:%S %Z %Y") for d in data]).strftime("%B %d %Y, %H:%M:%S")
	
	print str(len(users)) +" users tweeted between " + time_min+ " and " +time_max

problem2(sys.argv[1])