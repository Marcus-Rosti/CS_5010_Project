import openweather
from datetime import datetime
import urllib.request
import urllib.error

print("here")
# create client
ow = openweather.OpenWeather(cache=False)
print("there")
# find weather stations near me
#stations = ow.find_stations_near(
#            7.0,  # longitude
#            50.0, # latitude
#            100   # kilometer radius
#                )

stations = ow.find_stations_near(38.025754, -78.500800,10)
print("checking for stations")
# iterate results
for station in stations:
        print(station)

# get current weather at Cologne/Bonn airport
# (station id = 4885)
print(ow.get_weather(4885))

# historic weather
start_date = datetime(2013, 9, 10)
end_date = datetime(2013, 9, 15)

# default: hourly interval
print(ow.get_historic_weather(4885, start_date, end_date))

# raw data (resolution = "tick")
print(ow.get_historic_weather(4885, start_date, end_date, "tick"))

# daily aggregates
print(ow.get_historic_weather(4885, start_date, end_date, "day"))
