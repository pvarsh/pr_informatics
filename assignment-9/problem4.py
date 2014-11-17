import csv
import shapefile
import sys
import bokeh.plotting as bk
from bokeh.objects import HoverTool
from collections import OrderedDict
import bokeh.embed
import bokeh.resources
import math
import numpy as np

def getZipBorough(zipBoroughFilename):
  # Wrong: reads all complaints and keeps zips which have complaints.
  # Creates a zip_code to borough dictionary
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
   
def getZipCount(complaintsFile, zipBorough):
  badZips = set()
  zipCount = {}

  with open(complaintsFile, 'r') as f:
    reader = csv.reader(f)
    header = reader.next() # skip header row
    for complaint in reader:
      complaintZip = complaint[8]
      try:
        zipAsInt = int(complaintZip)
        zipAsStr = str(zipAsInt).zfill(5)
        if zipAsStr in zipBorough:
          if zipAsStr not in zipCount:
            zipCount[zipAsStr] = 0
          else:
            zipCount[zipAsStr] += 1
       #   
       # if complaint[3] in agencyToCount:
       #    agencyToCount[complaint[3]] += 1
       # else:
       #    agencyToCount[complaint[3]]
      except:
        badZips.add(complaint[8])
  #print zipCount
  return zipCount 
  
def gridCounts(complaint_file, n):
  north = 40.915
  east = -73.651
  south = 40.496
  west = -74.256
  
  width = east - west
  height = north - south

  grid = [[1 for cell in range(n)] for cell in range(n)] # 1 for log transform
  
  with open(complaint_file, 'r') as f:
    reader = csv.reader(f)
    header = reader.next()
    lat_ind = header.index("Latitude")
    lon_ind = header.index("Longitude")
    for row in reader:
      try:
        lat = float(row[lat_ind])
        lon = float(row[lon_ind])
      except:
        pass
      if lat < north and lat > south and lon < east and lon > west:
        col = int((lon - west)/( (east-west)/n ))
        row = int((lat - south)/( (north - south)/n ))
        grid[row][col] += 1
  #for row in grid:
  #  print row
  log_grid = [[math.log(count) for count in col] for col in grid]
  #for row in log_grid:
  #  print row 
  
  ### Gridlines
  vLines = [west + width/n * i for i in range(n+1)]
  hLines = [south + height/n * i for i in range(n+1)]
  ### Find centers of grid cells
  centersHorizontal = [west + width/n * (i+0.5) for i in range(n)]
  centersVertical = [south + height/n * (i + 0.5) for i in range(n)]
  centers_lon = centersHorizontal * n
  centers_lat = [x for x in centersVertical for i in range(n)]
  return {'counts': grid, 'log_counts': log_grid}, {'lon': centers_lon, 'lat': centers_lat}, {'vLines': vLines, 'hLines': hLines}

def drawPlot(shapeFilename, zipBorough, zipCount): 
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  # Creates a dictionary for zip: {lat_list: [], lng_list: []}.
  zipCodes = []
  polygons = {'lat_list': [], 'lng_list': [], 'centerLat_list': [], 'centerLon_list': []}
  
  record_index = 0
  for r in dat.iterRecords():
    currentZip = r[0]

    # Keeps only zip codes in NY area.
    if currentZip in zipBorough: # was in zipBorough:

      # Gets shape for this zip.
      shape = dat.shapeRecord(record_index).shape
      
      ### Only first polygon if non-contiguous zip codes
      #firstPoint = shape.parts[0]
      #if len(shape.parts) > 1:
      #  lastPoint = shape.parts[1]
      #else:
      #  lastPoint = len(shape.points)
      #zipCodes.append(currentZip)
      #points = shape.points[firstPoint : lastPoint]
      #
      ## Breaks into lists for lat/lng.
      #lngs = [p[0] for p in points]
      #lats = [p[1] for p in points]

      ## Calculate centers
      #center_lngs = min(lngs) + (max(lngs) - min(lngs))/2
      #center_lats = min(lats) + (max(lats) - min(lats))/2

      ## Store centroids for current part shape
      #polygons['centerLat_list'].append(center_lats)
      #polygons['centerLon_list'].append(center_lngs)

      ## Stores lat/lng for current zip shape.
      #polygons['lng_list'].append(lngs)
      #polygons['lat_list'].append(lats)
      
      ### All shapes for each zip code
      for part in range(len(shape.parts)):
        zipCodes.append(currentZip)
        start = shape.parts[part]
        if part == len(shape.parts) - 1:
          end = len(shape.points)
        else:
          end   = shape.parts[part + 1]
        points = shape.points[start : end]
        
        # Breaks into lists for lat/lng.
        lngs = [p[0] for p in points]
        lats = [p[1] for p in points]

        # Calculate centers
        center_lngs = min(lngs) + (max(lngs) - min(lngs))/2
        center_lats = min(lats) + (max(lats) - min(lats))/2

        # Store centroids for current part shape
        polygons['centerLat_list'].append(center_lats)
        polygons['centerLon_list'].append(center_lngs)

        # Stores lat/lng for current zip shape.
        polygons['lng_list'].append(lngs)
        polygons['lat_list'].append(lats)

    record_index += 1

  # Creates the Plot
  bk.output_file("problem4.html")
  bk.hold()
  
  north = 40.915
  east = -73.651
  south = 40.496
  west = -74.256
  
  width = east - west
  height = north - south

  x_range = [west - 0.05 * width, east + 0.05 * width]
  y_range = [south - 0.05 * height, north + 0.05 * height] 

  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"

  fig = bk.figure(title="311 Complaints by Zip Code", \
         tools=TOOLS, background_fill = "#f8f8f8", x_range = x_range, y_range = y_range, plot_height=800, plot_width = 1200)
  #circleSizes = [zipCount[zipCode] for zipCode in zipCodes]
  circleSizes = []
  for zipCode in zipCodes:
    if zipCode in zipCount:
      circleSizes.append(zipCount[zipCode])
    else:
      circleSizes.append(1) # for taking logs
  #print circleSizes
  #print "aaaaaaaaaaaaaaaaaaaaa: ", len(polygons['lng_list']), len(circleSizes)

  logCircleSizes = ((np.log(np.array(circleSizes)))**3.7) * 0.009 
  #print logCircleSizes
  logCircleSizes = list(logCircleSizes)
  

  #circleSizes = [x for x in range(len(zipCodes))]
  # Creates the polygons
  bk.patches(polygons['lng_list'], polygons['lat_list'], fill_color="#fee8c8", line_color="gray")

  bk.scatter(polygons['centerLon_list'], polygons['centerLat_list'], size = logCircleSizes, alpha = 0.4, line_color = None, fill_color = 'red')
  #circleSizes = [0.009 * (size ** 3.7) for size in circleSizes]
  #bk.scatter(centers['lon'], centers['lat'], size = circleSizes, alpha = 0.4, line_color = None, fill_color = 'red')
  
  #circleSizeArr = np.array(circleSizes)
  #maxSize = np.max(circleSizeArr)
  #circleSizeArr[circleSizeArr == 0] = 100
  #minSize = np.min(circleSizeArr)
  
  #legendN = 5
  #legendCircles = list(np.linspace(minSize, maxSize, legendN))
  #legendCounts = [str(int((size ** (1.0/3.7))/0.009)) + " complaints" for size in legendCircles]
  #fakeScatter = [0 for x in range(legendN)]
  #fakeScatterX = [-74.23 for x in range(legendN)]
  #fakeScatterXtext = [-74.23 + 0.05 for x in range(legendN)]
  #fakeScatterY = [40.8, 40.8 + 0.02, 40.8 + 0.036, 40.8 + 0.056,40.8 + 0.083]
  #bk.scatter(fakeScatterX, fakeScatterY, size = legendCircles, fill_color = 'red', line_color = None, alpha = 0.4)
  #bk.text(fakeScatterXtext[1:], fakeScatterY[1:], text = legendCounts[1:], angle = 0, text_align = "left", text_font_size = "7pt", text_baseline = 'middle')
  
  # Disable background grid
  bk.grid().grid_line_color = None
  bk.show()

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] + '<complaints> <zipboroughfilename> <shapefile>' 
  else:
    complaintFile = sys.argv[1]
    zipBoroughFile = sys.argv[2]
    shapeFile = sys.argv[3]
    
    
    zipBorough = getZipBorough(zipBoroughFile)
    zipCount = getZipCount(complaintFile, zipBorough)
    ### Work with CSV
    #zipAgencyCount = getZipAgencyCount(sys.argv[1], zipBorough)
    #zipColors, legendColors = problem2color(zipAgencyCount, sys.argv[4], sys.argv[5])
    #print "colors: ", zipColors
    #zipMaxAgency = {}
    #for zipCode in zipAgencyCount:
    #  maxAgency = max(zipAgencyCount[zipCode], key = zipAgencyCount[zipCode].get)
    #  maxComplaints = zipAgencyCount[zipCode][maxAgency]
    #  zipMaxAgency[zipCode] = (maxAgency, maxComplaints) 
    #grids, centers, gridLines = gridCounts(complaintFile, n) 

    ### Draw plot 
    drawPlot(shapeFile, zipBorough, zipCount)

