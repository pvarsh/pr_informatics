import sys
import csv
from collections import Counter

def problem4(file_1):
	ht_counter = Counter([item for sublist in [[row[i] for i in range(4, len(row))] for row in csv.reader(open(file_1))] for item in sublist])
	print "\n".join([key + ', ' + `ht_counter[key]` for key in [elem[0] for elem in sorted(ht_counter.items(), key = lambda (k, v): (-v, k))][0:10]])

problem4(sys.argv[1])
