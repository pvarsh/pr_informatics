import sys
import csv 
from datetime import datetime
from collections import Counter

def problem6(f):
	max_date = max(Counter([datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y").replace(minute = 0, second = 0)\
			for row in csv.reader(open(f))]).items(), key = lambda t:t[1])
	print max_date[0].strftime("%B %d %Y, %H") + 'h with %s tweets' %max_date[1]

problem6(sys.argv[1])
