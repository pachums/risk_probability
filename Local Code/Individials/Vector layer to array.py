"""
Description:
This module contains a method for changing a vector layer to array
"""

import ogr, gdal
import numpy as np
import os

vector_fn = '/opt/project/Scripts_procesados/Data/layer1.shp'

# Define pixel_size and NoData value of new raster
pixel_size = 25
NoData_value = 255

# Open the data source and read in the extent
source_ds = ogr.Open(vector_fn)
source_layer = source_ds.GetLayer()
source_srs = source_layer.GetSpatialRef()
x_min, x_max, y_min, y_max = source_layer.GetExtent()

# Create the destination data source
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)
target_ds = gdal.GetDriverByName('MEM').Create('', x_res, y_res, gdal.GDT_Byte)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band = target_ds.GetRasterBand(1)
band.SetNoDataValue(NoData_value)

# Rasterize
gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])

# Read as array
array = band.ReadAsArray()
print(array)


'''CONVERT POLYGON TO POINTS'''
polygon_fn = '/opt/project/Scripts_procesados/Data/layer1.shp'

# Define pixel_size which equals distance between points
pixel_size = 500

# Open the data source and read in the extent
source_ds = ogr.Open(polygon_fn)
source_layer = source_ds.GetLayer()
x_min, x_max, y_min, y_max = source_layer.GetExtent()

# Create the destination data source
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)
target_ds = gdal.GetDriverByName('GTiff').Create('temp.tif', x_res, y_res, gdal.GDT_Byte)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band = target_ds.GetRasterBand(1)
band.SetNoDataValue(255)

# Rasterize
gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])

# Read as array
array = band.ReadAsArray()

raster = gdal.Open('temp.tif')
geotransform = raster.GetGeoTransform()

# Convert array to point coordinates
count = 0
roadList = np.where(array == 1)
multipoint = ogr.Geometry(ogr.wkbMultiPoint)
for indexY in roadList[0]:
    indexX = roadList[1][count]
    geotransform = raster.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    pixelWidth = geotransform[1]
    pixelHeight = geotransform[5]
    Xcoord = originX+pixelWidth*indexX
    Ycoord = originY+pixelHeight*indexY
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(Xcoord, Ycoord)
    multipoint.AddGeometry(point)
    count += 1

# Write point coordinates to Shapefile
shpDriver = ogr.GetDriverByName("ESRI Shapefile")
if os.path.exists('/opt/project/Scripts_procesados/Data/points.shp'):
    shpDriver.DeleteDataSource('/opt/project/Scripts_procesados/Data/points.shp')
outDataSource = shpDriver.CreateDataSource('/opt/project/Scripts_procesados/Data/points.shp')
outLayer = outDataSource.CreateLayer('/opt/project/Scripts_procesados/Data/points.shp', geom_type=ogr.wkbMultiPoint)
featureDefn = outLayer.GetLayerDefn()
outFeature = ogr.Feature(featureDefn)
outFeature.SetGeometry(multipoint)
outLayer.CreateFeature(outFeature)
outFeature = None

# Remove temporary files
os.remove('temp.tif')