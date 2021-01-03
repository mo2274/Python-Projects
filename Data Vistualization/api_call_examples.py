import requests
import json
from plotly.graph_objs import Bar, Layout
from plotly import offline

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}

response = requests.get(url, headers)
data = response.json()
projects_names = []
projects_stars = []
links = []
for item in data['items']:
    projects_names.append(item['name'])
    projects_stars.append(int(item["stargazers_count"]))
    repo_url = item['html_url']
    links.append(f"<a href='{repo_url}'>{item['name']}</a>")


data  = [{
    'type' : 'bar',
    'x'    : links,
    'y'    : projects_stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = Layout(title='highest stars python projects on github')
offline.plot({'data': data, 'layout': my_layout}, filename='data6.html')


