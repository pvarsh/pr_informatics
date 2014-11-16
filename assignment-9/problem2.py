import csv
import shapefile
import sys
import bokeh.plotting as bk
from bokeh.objects import HoverTool
from collections import OrderedDict
import bokeh.embed
import bokeh.resources

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

def problem2color(zipAgencyCount, agency1, agency2):
  zipColor = {}
  minColor = 1
  maxColor = 0
  for zipCode in zipAgencyCount:
    agency1count = 0
    agency2count = 0
    if agency1 in zipAgencyCount[zipCode]:
      agency1count = zipAgencyCount[zipCode][agency1]
    if agency2 in zipAgencyCount[zipCode]:
      agency2count = zipAgencyCount[zipCode][agency2]
    
    if (agency1count + agency2count) == 0:
      colorCode = -1
    else:
      colorCode = float(agency1count)/(agency1count + agency2count)
    zipColor[zipCode] = colorCode
    if colorCode > maxColor:
      maxColor = colorCode
    if colorCode >= 0 and colorCode < minColor:
      minColor = colorCode
  #print "COLORS for polygons:"  
  for zipCode in zipColor:
    red = hex(int(zipColor[zipCode] * 255))[2:5]
    blue = hex(int((1 - zipColor[zipCode]) * 255))[2:5]
    color = "#"+red+"00"+blue
    #print color
    zipColor[zipCode] = color

  ### Legend colors
  #print "COLORS for legend:"
  legendColors = []
  colorRange = [x*(1.0/40) for x in range(41)]
  #print colorRange
  for color in colorRange:
    red = hex(int(color * 255))[2:5]
    red = red.zfill(2)
    #print "red: ", red
    blue = hex(int((1-color)*255))[2:5]
    blue = blue.zfill(2)
    #print "blue: ", blue, hex(int((1-color)*255))
    color = "#"+red+"00"+blue
    legendColors.append(color)
    #print color
  return zipColor, legendColors

def drawPlot(shapeFilename, zipBorough, zipMaxAgency, zipColors, legendColors, agency1, agency2):
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  # Creates a dictionary for zip: {lat_list: [], lng_list: []}.
  zipCodes = []
  hoverZip = []
  hoverAgency = []
  hoverComplaints = []
  polygons = {'lat_list': [], 'lng_list': [], 'centerLat_list': [], 'centerLon_list': []}

  record_index = 0
  for r in dat.iterRecords():
    currentZip = r[0]

    # Keeps only zip codes in NY area.
    if currentZip in zipMaxAgency: # was in zipBorough:
      # zipCodes.append(currentZip) # moving this line into the parts loop

      # Gets shape for this zip.
      shape = dat.shapeRecord(record_index).shape
      for part in range(len(shape.parts)):
        zipCodes.append(currentZip)
        hoverZip.append(currentZip)
        hoverAgency.append(zipMaxAgency[currentZip][0])
        hoverComplaints.append(zipMaxAgency[currentZip][1])
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

  # Palette
  ##d9d9d9
  brewer11 = ['#8dd3c7', '#ffffb3', '#bebada','#fb8072','#80b1d3','#fdb462','#b3de69','#fccde5','#d9d9d9','#bc80bd','#ccebc5']
  #brewer11 = ['#a6cee3', '#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99']

  #agencies = sorted(list({zipMaxAgency[zipCode] for zipCode in zipMaxAgency}))
  
  biggestComplaints = {}
  for zz, aa in zipMaxAgency.iteritems():
    if aa[0] in biggestComplaints:
      biggestComplaints[aa[0]] += 1
    else:
      biggestComplaints[aa[0]] = 1
  
  # sorting agencies by number of zip codes (to try to get better colors)
  agencies = list(biggestComplaints.iteritems())
  agencies = sorted(agencies, key = lambda x: x[1], reverse = True)
  agencies = [agency[0] for agency in agencies]
  
  # Assign colors to agencies 
  polygons['colors'] = [zipColors[zipCode] for zipCode in zipCodes]
  
  # Prepare hover
  #source = bk.ColumnDataSource(data=dict(hoverAgency=hoverAgency, hoverZip=hoverZip, hoverComplaintCount=hoverComplaintCount,))
  source = bk.ColumnDataSource(data=dict(hoverZip = hoverZip, hoverAgency = hoverAgency, hoverComplaints = hoverComplaints),)
  # Creates the Plot
  bk.output_file("problem2.html")
  bk.hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
  fig = bk.figure(title="311 Complaints by Zip Code", \
         tools=TOOLS, background_fill = "#f8f8f8")
         
  
  # Creates the polygons.
  bk.patches(polygons['lng_list'], polygons['lat_list'], fill_color=polygons['colors'], line_color="gray") 
  
  ### Zip codes as text on polygons 
  #for i in range(len(polygons['centerLat_list'])):
  #  y = polygons['centerLat_list'][i]
  #  x = polygons['centerLon_list'][i]
  #  zipCode = zipCodes[i]
  #  bk.text([x], [y], text=zipCode, angle=0, text_font_size="8pt", text_align="center", text_baseline="middle")
 
  fonts = ["Comic sans MS", "Papyrus", "Curlz", "Impact", "Zapf dingbats", "Comic sans MS", "Papyrus", "Curlz", "Impact", "Zapf Dingbats", "Comic sans MS"]
   
  ### Legend

  x = -74.25
  y = 40.8


  height = 0.003
  legend_box_y = y + 0.5 * height * len(legendColors) 
  bk.rect([x+0.032], [legend_box_y], width = 0.12, height = height*len(legendColors)*1.15, color = "#ffffff", line_color = "gray")
  #x = -74.25
  #y = 40.9
  for color in legendColors: 
  #  #print "Color: ", a
  #  #print "x:", x
  #  #print "y:", y
  # 
    bk.rect([x], [y], color = color, width=0.03, height=height)
    #bk.text([x], [y], text = agency, angle=0, text_font_size="7pt", text_align="center", text_baseline="middle")
    y = y + height 
  legend_bottom_y = 40.797
  legend_top_y = legend_bottom_y + 0.92 * height * len(legendColors)
  bk.text([-74.225], [legend_bottom_y], text = agency2, angle = 0, text_font_size = "7pt", text_align = "left")
  bk.text([-74.225], [legend_top_y], text = agency1, angle = 0, text_font_size = "7pt", text_align = "left")
  #bokeh.embed.components(fig, bokeh.resources.CDN)
  bk.show()

if __name__ == '__main__':
  if len(sys.argv) != 6:
    print 'Usage:'
    print sys.argv[0] + ' <complaints> <zipboroughfilename> <shapefile> <agency1> <agency2>'
    print '\ne.g.: ' + sys.argv[0] + ' data/nyshape.shp zip_borough.csv'
  else:
    zipBorough = getZipBorough(sys.argv[2])
    agency1 = sys.argv[4]
    agency2 = sys.argv[5]
    
    ### Work with CSV
    zipAgencyCount = getZipAgencyCount(sys.argv[1], zipBorough)
    zipColors, legendColors = problem2color(zipAgencyCount, sys.argv[4], sys.argv[5])
    #print "colors: ", zipColors
    zipMaxAgency = {}
    for zipCode in zipAgencyCount:
      maxAgency = max(zipAgencyCount[zipCode], key = zipAgencyCount[zipCode].get)
      maxComplaints = zipAgencyCount[zipCode][maxAgency]
      zipMaxAgency[zipCode] = (maxAgency, maxComplaints) 
    #zipMaxAgency = {zipCode: max(zipAgencyCount[zipCode], key = zipAgencyCount[zipCode].get) for zipCode in zipAgencyCount}
    #print zipMaxAgency
    ### Draw plot 
    drawPlot(sys.argv[3], zipBorough, zipMaxAgency, zipColors, legendColors, agency1, agency2)
