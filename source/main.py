# Plot queried data to heat map
# Libraries used -  Pandas, Geopandas, GeoPlot, Matplotlib, Shapely

import pandas as pd
import geopandas as gpd
import geoplot as gplt
import matplotlib.pyplot as mplt
from shapely.geometry import Point
import queryData as q
import locationScore as ls

# Store list of stations/station attributes and list of airports
stationList = q.queryWeatherJob()
airportList = q.queryAirportJob()
#locScores = [25] * 2723

# Store location score for each weather station
locScores = ls.calculateScores(stationList, airportList)

#Convert list of station coordinates and location scores to dataframe
coords = [(row[4],row[3]) for row in stationList]
df = pd.DataFrame(list(zip(locScores, coords)),
                  columns = ['score', 'coords'])

# Convert our dataframe to geodataframe using shapely
df['geometry'] = df.coords.apply(Point)
locations = gpd.GeoDataFrame(df)


# Store US map geodataframe
us_map = gpd.read_file(gplt.datasets.get_path('contiguous_usa'))

# Store base layer of map - Single Map Projection
#ax = gplt.polyplot(
#    us_map, projection=gplt.crs.AlbersEqualArea(),
#    edgecolor='black', facecolor='white',
#    figsize=(16,12)
#)

# Store baselayers - multimap projection
fig = mplt.figure(figsize=(16,12))
gs = fig.add_gridspec(1,2)
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])


# Plot point map with hue
gplt.pointplot(locations[locations['score'] < 30],
               hue='score',
               legend=True,
               ax=ax1
               #ax=ax
)
#Set title and print baselayer
ax1.set_title("Weather and Proximity to Airport Point Map")
gplt.polyplot(us_map, ax=ax1)

# Plot heat map using locations with a score below 10
gplt.kdeplot(locations[locations['score'] < 8],
             cmap = 'Reds',
             #projection = gplt.crs.AlbersEqualArea(),
             shade=True, shade_lowest=None, thresh=0.05,
             clip=us_map.geometry,
             ax=ax2
             #ax=ax
)
#Set title and print baselayer
ax2.set_title("Weather and Proximity to Airport Heat Map")
gplt.polyplot(us_map, ax=ax2)

# Show our map
mplt.show()
