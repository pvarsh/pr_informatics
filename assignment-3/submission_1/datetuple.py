from datetime import datetime
x = "Fri Sep 19 21:00:18 EDT 2014"
xdt = datetime.strptime(x, "%a %b %d %H:%M:%S %Z %Y")
print [xdt]
print x
print xdt.hour
print xdt.year
print xdt.minute
print xdt.second
print xdt.time
