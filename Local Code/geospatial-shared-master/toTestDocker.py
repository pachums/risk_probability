#print("Hello World")
import pdal
import gdal
import requests
'''
OGR TUTORIAL: https://pcjericks.github.io/py-gdalogr-cookbook/vector_layers.html
'''
import sys
import os
import pathlib

try:
  import ogr
  print('Import of ogr from osgeo worked.  Eureka!\n')
except:
  print('Import of ogr from osgeo failed\n\n')


''' FIRST PART '''
    ## Get List of Ogr Drivers Alphabetically
cnt = ogr.GetDriverCount()
formatsList = []  # Empty List
for i in range(cnt):
    driver = ogr.GetDriver(i)  #unintelligible code for driver
    driverName = driver.GetName() #proper name
    if not driverName in formatsList:
        formatsList.append(driverName)
formatsList.sort() # Sorting the messy list of ogr drivers
#for i in formatsList: print (i)

    ## Is Ogr Driver Available by Driver Name
driverName = "PostgreSQL" # More drivers: GPX, Geomedia, KML
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print("%s driver not available.\n" % driverName)
else:
    print("%s driver IS available.\n" % driverName)


    ##Check access to the file
count = 0
print(pathlib.Path(address).exists)
os.path.exists(os.path.join(address,".shp"))

# for path in pathlib.Path(address).iterdir():
#    if path.is_file():
#        count += 1
# print(count)

    ## Get Shapefile Feature Count
#path = os.getcwd()
#address= path + '/Scripts varios/'#Variable_Emisiones_ENP.shp' #/workspaces/Experimento\ 1\ \&\ 2/geospatial-shared-master/Scripts\ varios/Variable_Emisiones_ENP.shp' 
daShapefile = '/workspaces/Experimento 1 & 2/geospatial-shared-master/Scripts varios/Variable_Emisiones_ENP.shp' #'C://Users//Elvis//Documents//MEGAsync Downloads//CB//Codigos//Experimento 1 & 2//geospatial-shared-master//Scripts varios//Variable_Emisiones_ENP.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

# Check to see if shapefile is found.
if dataSource is None:
    print('Could not open %s \n' % (daShapefile))
else:
    print('Opened %s' % (daShapefile))
    layer = dataSource.GetLayer() #open layer, unintelligible code 
    featureCount = layer.GetFeatureCount()
    print("Number of features in %s: %d" % (layer.GetName(),featureCount))
    
    ## Get extent of a layer
extent=layer.GetExtent()
print('\nExtent:\nUL: ',extent[0],extent[3],'\nLR: ',extent[1],extent[2])

'''    ##Iterate over Features
for feature in layer:
    print(feature.GetField("SITE_NA")) #shows all ENP
layer.ResetReading() '''

    ##Get Geometry from each Feature in a Layer
for feature in layer:
    geom = feature.GetGeometryRef()
    #print(geom.Centroid().ExportToWkt()) #simplyfies the huge output
    
    ##Filter by attribute
layer.SetAttributeFilter("ODESIGN = 'Parque Nacional'")
for feature in layer:
    print (feature.GetField("SITE_NA"))


''' SECOND PART '''
print("\n-------------------SECOND PART-------------------")
    ##Save centroids of input Layer to an output Layer
# Get the input Layer
inShapefile = "C://Users//usuario//github//cloudmatrix20//Scripts varios//Variable_Emisiones_ENP.shp"
inDriver = ogr.GetDriverByName("ESRI Shapefile")
inDataSource = inDriver.Open(inShapefile, 0)
inLayer = inDataSource.GetLayer()

# Create the output Layer
outShapefile = "C://Users//usuario//github//cloudmatrix20//Scripts varios//ENP_centroids"
outDriver = ogr.GetDriverByName("ESRI Shapefile")

# Remove output shapefile if it already exists
if os.path.exists(outShapefile):
    outDriver.DeleteDataSource(outShapefile)

# Create the output shapefilel
outDataSource = outDriver.CreateDataSource(outShapefile)
outLayer = outDataSource.CreateLayer("ENP_centroids", geom_type=ogr.wkbPoint)


# Add input Layer Fields to the output Layer
inLayerDefn = inLayer.GetLayerDefn()

for i in range(0, inLayerDefn.GetFieldCount()): #22
    fieldDefn = inLayerDefn.GetFieldDefn(i) #store the field
    outLayer.CreateField(fieldDefn)

# Get the output Layer's Feature Definition
outLayerDefn = outLayer.GetLayerDefn()
'''
# Add features to the ouput Layer
for i in range(4, inLayer.GetFeatureCount()): #143
    # Get the input Feature
    inFeature = inLayer.GetFeature(i)
    # Create output Feature
    outFeature = ogr.Feature(outLayerDefn)
    # Add field values from input Layer
    for i in range(3, outLayerDefn.GetFieldCount()): #22
        outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(), inFeature.GetField(i))
    # Set geometry as centroid
    geom = inFeature.GetGeometryRef()
    inFeature = None
    centroid = geom.Centroid()
    outFeature.SetGeometry(centroid)
    # Add new feature to output Layer
    outLayer.CreateFeature(outFeature)
    outFeature = None
'''
    
# Save and close DataSources
inDataSource = None
outDataSource = None

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
