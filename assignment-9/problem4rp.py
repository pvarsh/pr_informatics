# Principles of Urban Informatics
# Assignment 9
# Student: Renate Pinggera, N10276804
# November 17, 2014

# ----------------------------------------------------------
# PROBLEM 4
# > python problem4.py data/311_Service_Requests_from_2010_to_Present.csv data/zip_borough.csv data/tl_2013_us_zcta510/tl_2013_us_zcta510.shp

import csv
import shapefile
import sys
import math
import operator
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers
from bokeh.objects import HoverTool
from collections import OrderedDict

def loadComplaints(complaintsFilename):
	# Reads all complaints and keeps zips which have complaints.
	with open(complaintsFilename) as f:
		csvReader = csv.reader(f)
		headers = csvReader.next()
		zipIndex = headers.index('Incident Zip')
		latColIndex = headers.index('Latitude')
		lngColIndex = headers.index('Longitude')
		agencyIndex = headers.index('Agency')

		lat = []
		lng = []  
	
		colors = []
		complaintsPerZip = {}

		for row in csvReader:
			try:
				lat.append(float(row[latColIndex]))
				lng.append(float(row[lngColIndex]))
				zipCode = row[zipIndex]
	  
				if zipCode in complaintsPerZip:
					complaintsPerZip[zipCode]+=1
				else:
					complaintsPerZip[zipCode]=1

			except:
				pass

		#print "complaintsPerZip: ", complaintsPerZip

	return {'zip_complaints': complaintsPerZip}


# In[9]:

def getZipBorough(zipBoroughFilename):
	# Reads all complaints and keeps zips which have complaints.
	with open(zipBoroughFilename) as f:
		csvReader = csv.reader(f)
		csvReader.next()

		return {row[0]: row[1] for row in csvReader}


# In[15]:

def drawPlot(shapeFilename, mapPoints, zipBorough):
	# Read the ShapeFile
	dat = shapefile.Reader(shapeFilename)
  
	# Creates a dictionary for zip: {lat_list: [], lng_list: []}.
	zipCodes = []
	polygons = {'lat_list': [], 'lng_list': [], 'color_list' : [], 'centerlat_list' : [] ,'centerlng_list' : [], 'radius_list' : []}

	hoverZip = list()
	hoverCompCount = list()
	hoverRadius = list()
	lngs10004 = list()
	lats10004 = list()
	
	# Top complaint number total
	sortedlist = sorted(mapPoints['zip_complaints'].items(), key=operator.itemgetter(1), reverse=True)
	complaintsHighestTotal = sortedlist[0][1]

	minRadius=0.00015
	maxRadius=0.015

	record_index = 0
	for r in dat.iterRecords():
		currentZip = r[0]

		# Keeps only zip codes in NY area.
		if currentZip in zipBorough:
			zipCodes.append(currentZip)

			# Gets shape for this zip.
			shape = dat.shapeRecord(record_index).shape
			points = shape.points

			# Breaks into lists for lat/lng.
			lngs = [p[0] for p in points]
			lats = [p[1] for p in points]

			# Stores lat/lng for current zip shape.
			polygons['lng_list'].append(lngs)
			polygons['lat_list'].append(lats)


			# Calculate circle radius, according to number of complaints
			if currentZip in mapPoints['zip_complaints']:
				compCount = mapPoints['zip_complaints'][currentZip]
				
				#print "compCount: ", compCount
				#print "complaintsHighestTotal: ", complaintsHighestTotal
				perc = float(compCount)/float(complaintsHighestTotal)
				#print "perc: ", perc
				relRadius = (maxRadius-minRadius)*perc
				#print "relRadius: ", relRadius
				color = '#C9C9C9'
			else:
				color = 'grey'
				compCount = 0
				relRadius = 0
				
			# we try to fix broken polygon for zip 10004
			# http://www.maptechnica.com/us-zip-code-boundary-map/zip/10004
			if currentZip == '10004':
				color = 'blue'
				lngs10004.append(lngs)
				lats10004.append(lats)
				#print "lngs10004:", lngs10004
				#print "lats10004:", lats10004
				
			# we try to find the center of polygon
			lngmiddle = min(lngs)+((max(lngs)-min(lngs))/2)
			latmiddle = min(lats)+((max(lats)-min(lats))/2)

			hoverZip.append(currentZip)
			hoverCompCount.append(compCount)
			hoverRadius.append(relRadius*100)
			polygons['color_list'].append(color)
			
			polygons['centerlat_list'].append(latmiddle)
			polygons['centerlng_list'].append(lngmiddle)
			polygons['radius_list'].append(relRadius)

		record_index += 1

	# http://bokeh.pydata.org/tutorial/solutions/gallery/hover.html
	# We need to put these data into a ColumnDataSource
	source = ColumnDataSource(
		data=dict(
			hoverZip=hoverZip,
			hoverCompCount=hoverCompCount,
			hoverRadius=hoverRadius,
		)
	)

	# Creates the Plot
	titleString = "Relative Number of Complaints"
	
	output_file("problem4.html", title=titleString)
  
	TOOLS="pan,wheel_zoom,box_zoom,reset,hover,previewsave"
	
	# Creates the polygons.
	patches(polygons['lng_list'], polygons['lat_list'], source=source, fill_color=polygons['color_list'], line_color="gray", tools=TOOLS, plot_width=1100, plot_height=700,			  title=titleString)
				  
	# RP: add hover
	hover = curplot().select(dict(type=HoverTool))
	hover.tooltips = OrderedDict([
		("Zip:", "@hoverZip"),
		("No. of Complaints:", "@hoverCompCount"),
		#("Radius:", "@hoverRadius"),
	])

	# and add the legend just next to the data
	hold()
 
	#x = -73.66
	#y = 40.50
	#rect([x], [y], color='blue', width=0.03, height=0.015)
	# for i in (range(noOfSteps)):
	# 	rect([x], [y], color=RGB_to_hex(colorGradient[i]), width=0.03, height=0.015)
	# 	text([x], [y], text=i, angle=0, text_font_size="8pt", text_align="center", text_baseline="middle")
	# 	if i == 0:
	# 		text([x], [y], text=a2, angle=0, text_font_size="8pt", text_align="center", text_baseline="middle")
	# 	elif i == 9:
	# 		text([x], [y], text=a1, angle=0, text_font_size="8pt", text_align="center", text_baseline="middle")
	# 	y = y + 0.015
		
	# RP: try to print a circle in the middle of each polygon
	circle(polygons['centerlng_list'], polygons['centerlat_list'], radius=polygons['radius_list'], 
		fill_color='red', fill_alpha=0.6, line_color=None)
	
	# RP try to print cicles for zip 10004 lat lng points
	circle(lngs10004[0], lats10004[0], radius=0.00015, fill_color='green',
		       line_color=None)
		
	text([lngs10004][0], [lats10004][0],
	    text=lngs10004,angle=0, text_color='#333333',
	    text_align="center", text_font_size="10pt")	
		
	show()



# In[6]:

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print 'Usage:'
		print sys.argv[0] \
		+ ' <shapefilename> <complaintsfilename> <zipboroughfilename>'
		print '\ne.g.: ' + sys.argv[0] \
		+ ' data/nyshape.shp data/complaints.csv zip_borough.csv'
	else:
		
		complaintsFile = sys.argv[1]
		zipBoroughsFile = sys.argv[2]
		shapeFile = sys.argv[3]

		mapPoints = loadComplaints(complaintsFile)
		zipBorough = getZipBorough(zipBoroughsFile)
		drawPlot(shapeFile, mapPoints, zipBorough)

