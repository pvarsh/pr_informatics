import sys
import csv 
from datetime import datetime
from collections import Counter

def problem7(f):
	with open(f) as f:
		data =[r for r in csv.reader(f)]
		max_user = max(Counter([row[0] for row in data]).items(), key = lambda t:t[1])
		time_min = min([datetime.strptime(d[1], "%a %b %d %H:%M:%S %Z %Y") for d in data]).strftime("%B %d %Y, %H:%M:%S")
		time_max = max([datetime.strptime(d[1], "%a %b %d %H:%M:%S %Z %Y") for d in data]).strftime("%B %d %Y, %H:%M:%S")
	
	print max_user[0], 'tweeted the most\nDataset range: ' + time_min +' and ' + time_max

problem7(sys.argv[1])
