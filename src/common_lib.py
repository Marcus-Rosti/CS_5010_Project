import json
import csv
import os.path
import logging
import time
import urllib.request


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
    start_time = max(times)

    #get the current time
    end_time = int(time.time())

    logger.debug('Returning \n\tfirst: ' + str(start_time) + \
                           '\n\tlast:  ' + str(end_time))
    return start_time, end_time


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

def extractor(start_time, end_time):
    logger.debug('Getting json between '+str(start_time)+' and '+str(end_time))
    # Create the url that needs to access
    url = "http://api.openweathermap.org/data/2.5/history/city?id=4752046&type=hour&start="+str(start_time)+"&end="+str(end_time)

    logger.debug('The Url:\n\t'+url)
    # Open the url
    response = urllib.request.urlopen(url)

    # Read-in the JSON file and return the value
    JSONFile = response.read()
    return JSONFile


def write_json_to_file(filename, json):
    # writes json to a file
    logger.debug('Writing json to file '+filename)
    f = open(filename, 'w')
    try:
        json = str(json)
        json = json[2:len(json)]
        json = json[0:len(json)-3]
        f.write(json)
    except Exception:
        logger.warning('Error writing to file')
        raise
        return False
    f.close()
    logger.debug('Successfully wrote to file')
    return True;
