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
    complaintTypeIndex = headers.index('Complaint Type')

    lat = []
    lng = []    
    colorscale = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a", "#ffff99", "#b15928"]

    complaintTypeDict = {}
    colors = []
    for row in csvReader:
      try:
        lat.append(float(row[latColIndex]))
        lng.append(float(row[lngColIndex]))
        complaintType = row[complaintTypeIndex]
        if not complaintType in complaintTypeDict:          
          complaintTypeDict[complaintType] = len(complaintTypeDict)
        colorIndex = complaintTypeDict[complaintType] % len(colorscale)
        colors.append(colorscale[colorIndex])
      except:
        pass

    return {'lat_list': lat, 'lng_list': lng, 'color_list': colors}


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
  polygons = {'lat_list': [], 'lng_list': []}

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

    record_index += 1


  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")
  # hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
  
  # Creates the polygons.
  patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color='#fee8c8', line_color="gray", \
          tools=TOOLS, plot_width=1100, plot_height=700, \
          title="Zip codes in NY")
                  
  # # Draws mapPoints on top of map.
  hold()
  #TODO: Apply transformation to lat/lng points: all fall in the same
  #position on the map.
  scatter(mapPoints['lng_list'], mapPoints['lat_list'],
          fill_color='red',color='red', fill_alpha=0.0, line_alpha=0.1, size=3, name="mapPoints")

  show()


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] \
    + ' <shapefilename> <complaintsfilename> <zipboroughfilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/nyshape.shp data/complaints.csv zip_borough.csv'
  else:
    mapPoints = loadComplaintsPoints(sys.argv[2])
    zipBorough = getZipBorough(sys.argv[3])
    drawPlot(sys.argv[1], mapPoints, zipBorough)
