import sys
import csv
from collections import Counter

def problem8(f):
	with open(f) as f:
		data = [r for r in csv.reader(f)]
	nyc_ht = [[r[i] for i in range(4, len(r))] for r in data if\
	(float(r[2]) >= -74.2557 and float(r[3]) >= 40.4957) and (float(r[2]) <= -73.6895 and float(r[3]) <= 40.9176)]
	sf_ht = [[r[i] for i in range(4, len(r))] for r in data if\
	(float(r[2]) >= -122.5155 and float(r[3]) >= 37.7038) and (float(r[2]) <= -122.3247 and float(r[3]) <= 37.8545)]
	nyc_count	= dict(Counter([item for sublist in nyc_ht for item in sublist]))
	sf_count	= dict(Counter([item for sublist in sf_ht for item in sublist]))
	print 'New York:\n'+"\n".join([key + ', ' + `nyc_count[key]` for key in [elem[0] for elem in sorted(nyc_count.items(), key = lambda (k, v): (-v, k))][0:5]])
	print 'San Francisco:\n' + "\n".join([key + ', ' + `sf_count[key]` for key in [elem[0] for elem in sorted(sf_count.items(), key = lambda (k, v): (-v, k))][0:5]])

problem8(sys.argv[1])