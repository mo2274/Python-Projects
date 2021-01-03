import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_name1 = r"data\death_valley_2018_simple.csv"
file_name2 = r"data\sitka_weather_07-2018_simple.csv"

def extract_dates():
    with open(file_name1) as fh:
        reader = csv.reader(fh)
        headers = next(reader, None)
        data = next(reader, None)
        dates = []
        while data:
            dates.append(datetime.strptime(data[2], '%Y-%m-%d'))
            data = next(reader, None)
    return (dates, headers)

def extract_data(field):
    with open(file_name1) as fh:
        reader = csv.reader(fh)
        data = next(reader, None)
        data = next(reader, None)
        highs = []
        while data:
            try:
                highs.append(int(data[field]))
                data = next(reader, None)
            except:
                highs.append(0)
                data = next(reader, None)
    return highs

def get_index(headers, d):
    for index, data in enumerate(headers):
        if data == d:
            h = index
    return h



dates, headers= extract_dates()
h = get_index(headers, 'TMAX')
l = get_index(headers, "TMIN")

highs = extract_data(h)
lows = extract_data(l)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=14)
ax.set_ylabel("Temperature", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=10)
fig.autofmt_xdate()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='black', alpha=0.5)
plt.show()
