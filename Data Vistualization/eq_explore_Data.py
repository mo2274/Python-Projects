import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


file_name = r"data\eq_data_30_day_m1.json"

with open(file_name) as fh:
    data_ = json.load(fh)

mags = []
lon = []
lat = []
titles = []
for earthquike in data_["features"]:
    mags.append(earthquike["properties"]["mag"])
    lon.append(earthquike["geometry"]["coordinates"][0])
    lat.append(earthquike["geometry"]["coordinates"][1])
    titles.append(earthquike["properties"]["title"])

data = [{
    'type': "scattergeo",
    'lon' : lon,
    'lat' : lat,
    'text': titles,
    'marker': {
        'size' : [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    } 
}]
my_layout = Layout(title=data_["metadata"]['title'])
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')