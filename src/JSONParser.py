#!/usr/bin/python3
import json
import csv
import os.path

def parseJSONFile(JSONFile):
	with open(JSONFile) as datafile:
		rawData = json.load(datafile)

	file = open("../data/testOutput.csv","a")	
	f = csv.writer(file,quotechar='"')

	if not (os.path.isfile("../data/testOutput.csv")):
		headers=["date_unix","main_temp","main_pressure","main_humidity","main_temp_min","main_temp_max","wind_speed","wind_deg","weather_main","weather_description","clouds"]
		f.writeheader()

	listData = rawData['list']
	

	for hourlyRecord in listData:
		date_unix = hourlyRecord['dt']
		main_temp = hourlyRecord['main']['temp']
		main_pressure = hourlyRecord['main']['pressure']
		main_humidity = hourlyRecord['main']['humidity']
		main_temp_min = hourlyRecord['main']['temp_min']
		main_temp_max = hourlyRecord['main']['temp_max']
		wind_speed = hourlyRecord['wind']['speed']
		wind_deg = hourlyRecord['wind']['deg']
		weather_main = hourlyRecord['weather'][0]['main']
		weather_description = hourlyRecord['weather'][0]['description']
		clouds  = hourlyRecord['clouds']['all']
		f.writerow([date_unix,main_temp,main_pressure,main_humidity,main_temp_min,main_temp_max,wind_speed,wind_deg,weather_main,weather_description,clouds])
	
	file.close()
	
parseJSONFile('../data/example.json')
