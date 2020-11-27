import gdal, ogr, osr
import numpy as np
import geopandas as gpd

def reproject(image, output_folder, epsg_to=3035, return_output_path = False):
    """
    This function reprojects a raster image

    :param image: path to raster image
    :param output_folder: output folder where the output image will be saved
    :param epsg_to: coordinate epsg code to reproject into
    :param return_output_path: If True, it returns the output path
    :return: returns a virtual data source
    """
    splitted = image.split("/")
    lenout = len(splitted)
    out_name = splitted[lenout-1]
    output = f"{output_folder}/reprojeted_{out_name}"

    dataset = gdal.Open(image)
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(epsg_to)
    vrt_ds = gdal.AutoCreateWarpedVRT(dataset, None, srs.ExportToWkt(), gdal.GRA_NearestNeighbour)

    # cols = vrt_ds.RasterXSize
    # rows = vrt_ds.RasterYSize
    gdal.GetDriverByName("GTiff").CreateCopy(output, vrt_ds)

    if return_output_path:
        return(output)
    else:
        return(vrt_ds)

if __name__ == '__main__':
    #raster = r'/workspaces/cloudmatrix20/SentinelAsturias/S2A_MSIL2A_20190919T110721_N0213_R137_T30TUN_20190919T140654/S2A_MSIL2A_20190919T110721_N0213_R137_T30TUN_20190919T140654.SAFE/GRANULE/L2A_T30TUN_A022156_20190919T111421/IMG_DATA/R20m/T30TUN_20190919T110721_B02_20m.jp2'
    raster = '/opt/project/SentinelAsturias/S2A_MSIL2A_20190919T110721_N0213_R137_T30TUN_20190919T140654/S2A_MSIL2A_20190919T110721_N0213_R137_T30TUN_20190919T140654.SAFE/GRANULE/L2A_T30TUN_A022156_20190919T111421/IMG_DATA/R20m/T30TUN_20190919T110721_B02_20m.jp2'
    output_folder = '/opt/project/SentinelAsturias/S2A_MSIL2A_20190919T110721_N0213_R137_T30TUN_20190919T140654/S2A_MSIL2A_20190919T110721_N0213_R137_T30TUN_20190919T140654.SAFE/GRANULE/L2A_T30TUN_A022156_20190919T111421/IMG_DATA/R20m'
    reproject(raster,output_folder)