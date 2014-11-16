import csv
import shapefile
import sys
import math
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

    lat = []
    lng = []  
    
    colors = []
    complaintsPerZip = {}
    maxComplaints = 0
    for row in csvReader:
      try:
        lat.append(float(row[latColIndex]))
        lng.append(float(row[lngColIndex]))
        zipCode = row[zipIndex]


        if zipCode in complaintsPerZip:
          complaintsPerZip[zipCode]+=1
        else:
          complaintsPerZip[zipCode]=1

        maxComplaints = max(complaintsPerZip[zipCode], maxComplaints)


      except:
        pass

    return {'zip_complaints': complaintsPerZip, 'max_complaints' : maxComplaints}


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
  colorscale = ["#fff7ec", "#fee8c8", "#fdd49e", "#fdbb84", "#fc8d59", "#ef6548", "#d7301f", "#b30000", "#7f0000"]

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
        colorIndex = ((mapPoints['zip_complaints'][currentZip]-1) / float(mapPoints['max_complaints'])) * len(colorscale)
        color = colorscale[int(colorIndex)]
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
