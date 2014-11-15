import csv
import shapefile
import sys
import bokeh.plotting as bk

def getZipBorough(zipBoroughFilename):
  # Wrong: reads all complaints and keeps zips which have complaints.
  # Creates a zip_code to borough dictionary
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
  

def drawPlot(shapeFilename, zipBorough):
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
      for part in range(len(shape.parts)):
        start = shape.parts[part]
        if part == len(shape.parts) - 1:
          end = len(shape.points)
        else:
          end   = shape.parts[part + 1]
          
        points = shape.points[start : end]

      # Breaks into lists for lat/lng.
        lngs = [p[0] for p in points]
        lats = [p[1] for p in points]

      # Stores lat/lng for current zip shape.
        polygons['lng_list'].append(lngs)
        polygons['lat_list'].append(lats)

    record_index += 1


  # Creates the Plot
  bk.output_file("zipCodes.html")
  bk.hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
  bk.figure(title="Zip codes in NY", \
         tools=TOOLS, plot_width=1200, plot_height=800)
  
  # Creates the polygons.
  bk.patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color='#fee8c8', line_color="gray")


  bk.show()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print 'Usage:'
    print sys.argv[0] + ' <complaints>' + ' <zipboroughfilename>'
    print '\ne.g.: ' + sys.argv[0] + ' data/nyshape.shp zip_borough.csv'
  else:
    zipBorough = getZipBorough(sys.argv[2])
    #zipBorough = {'10004':'Manhattan'}
    #zipBorough.pop('10004')

    ### Draw plot 
    #drawPlot(sys.argv[1], zipBorough)
    
    ### Work with CSV
    badZips = set()
    zipAgencyCount = {zipCode : {} for zipCode in zipBorough}    

    print "CSV"
    complaintsFile = "311_Service_Requests_from_2010_to_Present.csv" 
    with open(complaintsFile, 'r') as f:
      reader = csv.reader(f)
      header = reader.next() # skip header row
      for field in ['Agency', 'Incident Zip']:
        print(field, header.index(field))
      for complaint in reader:
        complaintZip = complaint[8]
        complaintAgency = complaint[3]
        try:
          zipAsInt = int(complaintZip)
          zipAsStr = zipAsInt.zfill(5)
          if zipAsStr in zipBorough:
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
         
    print badZips
    for badZip in badZips:
      try:
        print(int(badZip))
      except:
        pass
    print zipAgencyCount 
