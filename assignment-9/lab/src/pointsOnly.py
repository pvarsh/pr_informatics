import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers

def loadComplaintsPoints(complaintsFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(complaintsFilename) as f:
    csvReader = csv.reader(f)
    headers = csvReader.next()
    latColIndex = headers.index('Latitude')
    lngColIndex = headers.index('Longitude')

    lat = []
    lng = []

    for row in csvReader:
      try:
        lat.append(float(row[latColIndex]))
        lng.append(float(row[lngColIndex]))
      except:
        pass

    return {'lat_list': lat, 'lng_list': lng}

  

def drawPlot(mapPoints):
  

  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")
  # hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"

  # # Draws mapPoints on top of map.
  hold()
  #TODO: Apply transformation to lat/lng points: all fall in the same
  #position on the map.
  scatter(mapPoints['lng_list'], mapPoints['lat_list'],
          fill_color='red',color='red', fill_alpha=1.0, line_alpha=0.1, size=3, tools=TOOLS, plot_width=1100, plot_height=700, name="mapPoints")

  show()


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print 'Usage:'
    print sys.argv[0] \
    + ' <complaintsfilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/complaints.csv'
  else:
    mapPoints = loadComplaintsPoints(sys.argv[1])
    drawPlot(mapPoints)
