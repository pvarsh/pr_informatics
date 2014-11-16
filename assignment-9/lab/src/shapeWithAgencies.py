import csv
import shapefile
import sys
import math
import operator
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers

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
    
    agencyDict = {}
    colors = []
    complaintsPerZip = {}

    for row in csvReader:
      try:
        lat.append(float(row[latColIndex]))
        lng.append(float(row[lngColIndex]))
        agency = row[agencyIndex]
        zipCode = row[zipIndex]
        if not agency in agencyDict:          
          agencyDict[agency] = len(agencyDict)


        if zipCode in complaintsPerZip:
          if agency in complaintsPerZip[zipCode]:
            complaintsPerZip[zipCode][agency]+=1
          else:
            complaintsPerZip[zipCode][agency]=1
        else:
          complaintsPerZip[zipCode]={}
          complaintsPerZip[zipCode][agency]=1

      except:
        pass

    return {'zip_complaints': complaintsPerZip}


def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
  

def drawPlot(shapeFilename, mapPoints, zipBorough):
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  # Creates a dictionary for zip: {lat_list: [], lng_list: []}.
  zipCodes = []
  polygons = {'lat_list': [], 'lng_list': [], 'color_list' : []}

  # Qualitative 6-class Set1
  colors = {'NYPD' : 'blue',
            'DOT' : 'yellow',
            'DOB' : 'purple',
            'DOE' : 'green',
            'HPD' : 'orange'}

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


      # Calculate color, according to number of complaints
      if currentZip in mapPoints['zip_complaints']:

        # Top complaint type
        sortedlist = sorted(mapPoints['zip_complaints'][currentZip].items(), key=operator.itemgetter(1), reverse=True)
        agency = sortedlist[0][0]

        #print currentZip, agency

        if agency in colors:
          color = colors[agency]
        else:
          color = 'white'

      else:
        color = 'white'
      polygons['color_list'].append(color)



    record_index += 1


  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")
  # hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"

  # Creates the polygons.
  patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color=polygons['color_list'], line_color="gray", \
          tools=TOOLS, plot_width=1100, plot_height=700, \
          title="Zip codes in NY")
                  
  show()


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] \
    + ' <shapefilename> <complaintsfilename> <zipboroughfilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/nyshape.shp data/complaints.csv zip_borough.csv'
  else:
    mapPoints = loadComplaints(sys.argv[2])
    zipBorough = getZipBorough(sys.argv[3])
    drawPlot(sys.argv[1], mapPoints, zipBorough)
