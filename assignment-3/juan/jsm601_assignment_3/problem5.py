import sys
import csv 
from datetime import datetime
from collections import Counter

def problem5(f):
	max_date = max(Counter([datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y") for row in csv.reader(open(f))]).items(), key = lambda t:t[1])
	print max_date[0].strftime("%B %d %Y, %H:%M:%S"), 'with %s tweets' %max_date[1]

problem5(sys.argv[1])