"""
Description:
This module contains a method for obtaining the extent of a layer or raster
"""

import gdal, ogr, osr
import numpy as np

def get_layerextent(layer_path):
    """
    Return the extent of layer with GPKG or ESRI Shapefile formats
    :param layer_path: Path to the layer
    :return: String with xmin, ymin, xmax and ymax coordinates.
    """
    longitud = len(layer_path.split("."))
    driver_name = layer_path.split(".")[longitud - 1]
    if driver_name == "gpkg":
        driver = ogr.GetDriverByName("GPKG")
    if driver_name == "shp":
        driver = ogr.GetDriverByName("ESRI Shapefile")

    ds = driver.Open(layer_path)
    xmin, xmax, ymin, ymax = ds.GetLayer().GetExtent()
    extent = f"{xmin}, {ymin}, {xmax}, {ymax}"

    del ds
    print(extent)

def get_rasterextent(raster, dictionary = False):
    """
    Get the extent of a raster image
    :param raster: Path to the raster file
    :param dictionary: If True, a dictionary with the path of the raster as key and the extent of the raster as value is returned.
    :return: The extent with next order: xmin, xmax, ymin and ymax coordinates
    """

    r = gdal.Open(raster)
    ulx, xres, xskew, uly, yskew, yres = r.GetGeoTransform()
    lrx = ulx + (r.RasterXSize * xres)
    rly = uly + (r.RasterYSize * yres)

    # xmin, xmax, ymin and ymax
    extent = [ulx, lrx, rly, uly]
    print(extent)

    if dictionary:
        return({raster: extent})
    else:
        return (extent)

if __name__ == '__main__':
    raster='/opt/project/SentinelAsturias/S2A_MSIL2A_20200529T112121_N0214_R037_T29TQJ_20200529T121613/S2A_MSIL2A_20200529T112121_N0214_R037_T29TQJ_20200529T121613.SAFE/GRANULE/L2A_T29TQJ_A025774_20200529T112609/IMG_DATA/R20m/T29TQJ_20200529T112121_B02_20m.jp2'
    layer_path="/opt/project/Variable_Emisiones_ENP.shp"
    get_rasterextent(raster)
    get_layerextent(layer_path)

