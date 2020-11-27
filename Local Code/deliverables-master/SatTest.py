print("Hello World")
import pandas
import geopandas
import rasterio
from rasterio import plot
import matplotlib
# %matplotlab inline
pathSat = '/workspaces/Experimento 1 & 2/deliverables-master/sentinel_2_SE'

#blue
band2 = rasterio.open(pathSat + '/T30SXH_20200828T105031_B02.jp2', driver='JP2OpenJPEG')
#green
band3 = rasterio.open(pathSat + '/T30SXH_20200828T105031_B03.jp2', driver='JP2OpenJPEG')
#red
band4 = rasterio.open(pathSat + '/T30SXH_20200828T105031_B04.jp2', driver='JP2OpenJPEG')
#near-infrared (nir)
band8 = rasterio.open(pathSat + '/T30SXH_20200828T105031_B08.jp2', driver='JP2OpenJPEG')

#Bands that contains (should be 1)
print(band4.count)

#colums
print(band4.width)

#rows
print(band4.height)

#Plot matrix array
plot.show(band4)


