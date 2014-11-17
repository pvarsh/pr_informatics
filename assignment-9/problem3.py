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
   
def getZipAgencyCount(complaintsFile, zipBorough):
  badZips = set()
  zipAgencyCount = {}

  with open(complaintsFile, 'r') as f:
    reader = csv.reader(f)
    header = reader.next() # skip header row
    for complaint in reader:
      complaintZip = complaint[8]
      complaintAgency = complaint[3]
      try:
        zipAsInt = int(complaintZip)
        zipAsStr = str(zipAsInt).zfill(5)
        if zipAsStr in zipBorough:
          if zipAsStr not in zipAgencyCount:
            zipAgencyCount[zipAsStr] = {}
          if complaintAgency in zipAgencyCount[zipAsStr]:
            zipAgencyCount[zipAsStr][complaintAgency] += 1
          else:
            zipAgencyCount[zipAsStr][complaintAgency] = 1
            
       #   
       # if complaint[3] in agencyToCount:
       #    agencyToCount[complaint[3]] += 1
       # else:
       #    agencyToCount[complaint[3]]
      except:
        badZips.add(complaint[8])
  return zipAgencyCount 
  
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

def drawPlot(shapeFilename, zipBorough, grids, centers, gridLines):
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
  bk.output_file("problem3.html")
  bk.hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
  fig = bk.figure(title="311 Complaints by Zip Code", \
         tools=TOOLS, background_fill = "#f8f8f8")
  #print "aaaaaaaaaaaaaaa" 
  #print grids['log_counts']
  circleSizes = [item for sublist in grids['log_counts'] for item in sublist]
  #circleSizes = [item for sublist in grids['counts'] for item in sublist]
  #print circleSizes

  #print "aaaaaaaaaaaaaaa" 
  # Creates the polygons
  cellWidth = gridLines['vLines'][1]-gridLines['vLines'][0]
  cellHeight = gridLines['hLines'][1] - gridLines['hLines'][0]
  bk.patches(polygons['lng_list'], polygons['lat_list'], fill_color="#fee8c8", line_color="gray")
  for i in range(len(centers['lat'])):
    #print centers['lat'][i], centers['lon'][i]
    bk.rect([centers['lon'][i]], [centers['lat'][i]], fill_color = None, width = cellWidth, height = cellHeight, line_color = '#d5d5d5') 
    bk.circle([centers['lon'][i]], [centers['lat'][i]], fill_color = 'red', size = .009 * (circleSizes[i])**3.7, line_color = None, alpha = 0.4)
  bk.grid().grid_line_color = None
  #print centers 
  ### Legend
  #x = -74.25
  #y = 40.8
  #height = 0.003
  #legend_box_y = y + 0.5 * height * len(legendColors) 
  #bk.rect([x+0.032], [legend_box_y], width = 0.12, height = height*len(legendColors)*1.15, color = "#ffffff", line_color = "gray")
  ##x = -74.25
  ##y = 40.9
  #for color in legendColors: 
  ##  #print "Color: ", a
  ##  #print "x:", x
  ##  #print "y:", y
  ## 
  #  bk.rect([x], [y], color = color, width=0.03, height=height)
  #  #bk.text([x], [y], text = agency, angle=0, text_font_size="7pt", text_align="center", text_baseline="middle")
  #  y = y + height 
  #legend_bottom_y = 40.797
  #legend_top_y = legend_bottom_y + 0.92 * height * len(legendColors)
  #bk.text([-74.225], [legend_bottom_y], text = agency2, angle = 0, text_font_size = "7pt", text_align = "left")
  #bk.text([-74.225], [legend_top_y], text = agency1, angle = 0, text_font_size = "7pt", text_align = "left")
  #bokeh.embed.components(fig, bokeh.resources.CDN)
  
  bk.show()

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] + ' <complaints> <zipboroughfilename> <shapefile>' 
  else:
    complaintFile = sys.argv[1]
    zipBoroughFile = sys.argv[2]
    shapeFile = sys.argv[3]
    
    zipBorough = getZipBorough(zipBoroughFile)
    ### Work with CSV
    #zipAgencyCount = getZipAgencyCount(sys.argv[1], zipBorough)
    #zipColors, legendColors = problem2color(zipAgencyCount, sys.argv[4], sys.argv[5])
    #print "colors: ", zipColors
    #zipMaxAgency = {}
    #for zipCode in zipAgencyCount:
    #  maxAgency = max(zipAgencyCount[zipCode], key = zipAgencyCount[zipCode].get)
    #  maxComplaints = zipAgencyCount[zipCode][maxAgency]
    #  zipMaxAgency[zipCode] = (maxAgency, maxComplaints) 
    grids, centers, gridLines = gridCounts(complaintFile, 16) 

    ### Draw plot 
    drawPlot(shapeFile, zipBorough, grids, centers, gridLines)

