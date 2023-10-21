from pandas_geojson import read_geojson
from tabulate import tabulate
import geopandas as gpd


txDot_Cities = gpd.read_file(filename = "ZipCodes.geojson", driver="GeoJSON")
test = txDot_Cities[txDot_Cities['name'] == 'Austin']

print(tabulate(test, headers='keys', tablefmt='psql'))