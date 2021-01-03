from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die = Die()
result = []
for i in range(100):
    result.append(die.roll())

d = dict()
for i in result:
    d[i] = d.get(i, 0) + 1

x = [i for i in range(die.num_sides)]
data  = [Bar(x=x,  y=list(d.values()))]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')