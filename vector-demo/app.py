from greppo import app
import geopandas as gpd


app.display(name='title', value='Austin, Texas Waste Dashboard')
app.display(name='description',
            value='A Greppo demo app for vector data using open source geojson data for the city of Austin, Texas.'
                  'This dashboard shows ')

app.base_layer(
    name="Open Street Map",
    visible=True,
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    subdomains=None,
    attribution='(C) OpenStreetMap contributors',
)

app.base_layer(
    provider="CartoDB Positron",
)

recycle_points = gpd.read_file(filename = "./vector-demo/RecycleLocations.geojson", driver="GeoJSON")

austinJurisdictions = gpd.read_file(filename = "./vector-demo/Austin_jurisdictions_20231021.geojson", driver="GeoJSON")
austinTexas = austinJurisdictions[austinJurisdictions['jurisdiction_type'] == 'FULL']

landfill_points = gpd.read_file(filename = "./vector-demo/LandfillsLocation.geojson")
landfill_points = landfill_points.drop(columns=['DATE_ADDED_DATA'])


app.vector_layer(
    data = austinTexas,
    name = "Austin, Texas city boundary",
    description = "A polygon showing Austin's city boundary.",
    style = {"fillColor": "#4daf4a"},
)


app.vector_layer(
    data=recycle_points,
    name="Recycle Facilities in Austin",
    description="Points showing where to recycle in Austin, TX.",
    style={"color": "#377eb8"},
)

app.vector_layer(
    data=landfill_points,
    name="Landfills in Austin",
    description="Points showing where landfills are in Austin, TX.",
    style={"color": "#ff0000"},
)




text_1 = """
## About the web-app
The dashboard shows the city boundary of Austin, Texas as a vector polygon and landfills and recycle facilities as vector points.
"""

app.display(name='text-1', value=text_1)

app.display(name='text-2',
            value='The following displays the count of landfills and recycle facilities as a barchart.')


app.bar_chart(
    name="Geometry Count",
    description="Total number of Landfills and Recycle Facilities",
    x = [' ', 'Landfills', 'Recycle'],
    y=[0, len(landfill_points),len(recycle_points)],
    color=["#ff0000", "#ff0000", "#377eb8"],
)

