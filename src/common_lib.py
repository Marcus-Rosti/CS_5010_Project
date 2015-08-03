import json
import csv
import os.path
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/controller.log',level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def update(filename):
    logger.debug('Updating dates for file: '+filename)
    #returns last date and current date in unix time

    #pull the last date from the file
    #reads in all the times and finds the max
    times = []
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        next(lines, None) #skips the header
        for line in lines:
            times.append(int(line[0]))
    last = max(times)

    #get the current time
    import time
    current = int(time.time())

    logger.debug('Returning last: '+str(last)+' and first: ' + str(current))
    return last, current


def parseJSONFile(JSONFile, output_file):
    logger.debug('Parsing file: ' + JSONFile)
    with open(JSONFile) as datafile:
            rawData = json.load(datafile)

    file = open(output_file,"a")
    # file = open("../data/testOutput.csv","a")
    f = csv.writer(file,quotechar='"')

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
        f.writerow([date_unix,main_temp,main_pressure,main_humidity,main_temp_min,main_temp_max,wind_speed,wind_deg,weather_main,weather_description])

    logger.debug('Finished parsing file')
    file.close()

parseJSONFile("../data/example.json")
