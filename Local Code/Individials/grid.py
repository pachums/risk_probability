import gdal, ogr, osr
import numpy as np
import geopandas as gpd
import shapefile as shp

def createGrid(path_to_layer, spacing = 10000, epsg = 25830, buffer = None, output=None):
    """
    Creates a grid from a layer extent.
    :param path_to_layer: Path to layer
    :param spacing: Spacing of the grid cells (it applies to x and y)
    :param epsg: EPSG code of the coordinate
    :param buffer: Buffer to apply to the extent coordinates
    :param output: If defined, it creates an output.
    :return: Grid in geopandas format
    """

    gdf = gpd.read_file(path_to_layer)
    xmin, ymin, xmax, ymax = gdf.total_bounds # bounds of the total geometry

    # To be sure the bounding box created has all the set of points inside and it is multiple of the spacing.

    ytop = np.ceil(np.ceil(ymax) / spacing) * spacing
    ybottom = np.floor(np.floor(ymin) / spacing) * spacing
    xright = np.ceil(np.ceil(xmax) / spacing) * spacing
    xleft = np.floor(np.floor(xmin) / spacing) * spacing

    # Defining number of rows and columns
    rows = int((ytop - ybottom) / spacing)
    cols = int((xright - xleft) / spacing)

    polygons = []
    it = 0
    listfid = []
    for i in np.arange(xleft, xright, spacing):
        xleft = i
        xright = xleft + spacing
        ytop_backup = ytop
        for j in np.arange(ytop, ybottom, -spacing):
            ytop = j
            ybottom = ytop - spacing

            polygon = shp.geometry.Polygon([
                (xleft, ytop),
                (xright, ytop),
                (xright, ybottom),
                (xleft, ybottom)
            ]
            )
            polygons.append(polygon)
            listfid.append(it)
            it += 1
        ytop = ytop_backup
        # print(f"xleft: {xleft} xright: {xright} \n ytop: {ytop} ybottom: {ybottom}")

    # print(polygons)
    srs = f"epsg:{epsg}"
    fid = pd.DataFrame({"fid_id": listfid})
    grid = gpd.GeoDataFrame(fid, geometry=polygons, crs={"init": srs})

    if output is not None:
        print("Writing grid into disk")
        grid.to_file(output, driver="GPKG")

    #################################################
    ## BETTER TO RETURN JUST INTERSECTING POLYGONS ##
    #################################################
    if buffer:
        buf = grid.geometry.buffer(buffer)
        envelope = buf.envelope
        return(envelope)
    else:
        return(grid)

if __name__ == '__main__':
    #path_to_layer=r'/workspaces/cloudmatrix20/SentinelAsturias/CCAA/Provincias_España_VM.shp'
    path_to_layer=r'/opt/project/SentinelAsturias/CCAA/Provincias_España_VM.shp'
    createGrid(path_to_layer)       