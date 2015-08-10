""" Common library that contains methods used to fetch and prepare weather data

    List of methods:
		update(filename) - returns start and end times of missing weather data.
            Indicates date range for which data needs to be fetched.
		gap_filler(filename) - finds and returns gaps in the data.
		extractor(start_time, end_time) - fetches weather data between
            start_time and end_time. Returns weather data in JSON format.
		write_json_to_file(filename, json_text) - writes a string
            in json format to a file.
		parseJSONFile(JSON_File, output_file) - reads a JSON File,
            extracts relevant weather data and appends data to a CSV file

    These methods are called from controller.py

    Logs print to $Project_home/logs/controller.log
"""

import json
import csv
import os.path
import logging
import time
import urllib.request


LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/controller.log', level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def update(filename):
    """
        Reads a CSV input file and returns the time range for which data is
            missing at the end of the file. i.e.
            (Current time - last available time)
        This time range can be used to fetch required data from the API.

        Parameters:
            filename: CSV file containing previous weather data.
                      If previous weather data is not available,
                    the file should contain just the header row.

        Return Values:
            start_time, end_time: Unix Time values,
                between which data is not available in the CSV file.

    """
    LOGGER.debug('Updating dates for file: '+filename)
    #returns last date and current date in unix time, zeros if within an hour

    #reads in all the times and finds the max
    times = []
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        next(lines, None) #skips the header
        for line in lines:
            if line == []:
                continue
            times.append(int(line[0]))


    #get the current time
    end_time = int(time.time())

    if times == []:
        return 0, end_time
    else:
        start_time = max(times)

    LOGGER.debug('Returning \n\tfirst: ' + str(start_time) + \
                           '\n\tlast:  ' + str(end_time))

    #check to see if the times are an hour apart or more

    if end_time-start_time > 3600:
        return start_time+300, end_time
    else:
        return 0, 0

def gap_filler(filename):
    """
        Reads a CSV input file and returns the time range of the largest
            gap in the existing data.
        This time range can be used to fetch required data from the API.

        Parameters:
            filename:               CSV file containing previous weather data.
        Return Values:
            start_time, end_time:   Unix Time values, between
                                    which data is missing in the CSV file.

    """
    #Finds the largest gap in the record
    #returns the first and last date on either side of the gap, in unix time
    #Returns zeros  if nothing larger than an hour

    #reads in all the times
    times = []
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        next(lines, None) #skips the header
        for line in lines:
            times.append(int(line[0]))
    #sort the times
    times.sort()
    #Itterate over the loop, finding the max gap and position
    i = j = k = 0
    while i < len(times)-1:
        if times[i+1] - times[i] > k:
            j = i
            k = times[i+1]-times[i]
        i += 1

    #See if the gap is larger than an hour
    if k <= 3600:
        return 0, 0
    else:
        return times[j]+300, times[j+1]-300

def parseJSONFile(json_file, output_file):
    """
        Reads a JSON File, extracts relevant weather data
            and appends data to a CSV file.
        The following data is extracted from JSON:
                Unix Time, Temperature, Pressure, Humidity,
                Minimum Temperature, Maximum Temperature,
                Wind Speed, Wind Degree, Weather, Weather Description,
                Cloud Cover

        Parameters:
           json_file:    JSON file in standard format containing weather data.
           output_file: CSV file to which results should be appended.

        No Return Values

    """
    LOGGER.debug('Parsing file: ' + json_file)
    with open(json_file) as datafile:
        raw_data = json.load(datafile)

    file = open(output_file, "a")
    # file = open("../data/testOutput.csv","a")
    csv_writer = csv.writer(file, quotechar='"')

    list_data = raw_data['list']

    for hourly_recorded in list_data:
        date_unix = hourly_recorded['dt']
        main_temp = hourly_recorded['main']['temp']
        main_pressure = hourly_recorded['main']['pressure']
        main_humidity = hourly_recorded['main']['humidity']
        main_temp_min = hourly_recorded['main']['temp_min']
        main_temp_max = hourly_recorded['main']['temp_max']
        wind_speed = hourly_recorded['wind']['speed']
        wind_deg = hourly_recorded['wind']['deg']
        weather_main = hourly_recorded['weather'][0]['main']
        weather_description = hourly_recorded['weather'][0]['description']
        clouds = hourly_recorded['clouds']['all']
        csv_writer.writerow([date_unix, main_temp, main_pressure, \
            main_humidity, main_temp_min, main_temp_max, wind_speed, wind_deg, \
            weather_main, weather_description, clouds])

    LOGGER.debug('Finished parsing file')
    file.close()

def extractor(start_time, end_time):
    """
        Fetches weather data between a specified time range from
            Open Weather Map API (http://openweathermap.org/)

        Parameters:
           start_time:  Unix Time which specifies the start
                            of the time range for which
                            weather data should be fetched.
           end_time:    Unix Time which specifies the end of
                            the time range for which weather
                            data should be fetched.

        Return Values:
           string containing weather data encoded in JSON

    """
    LOGGER.debug('Getting json between '+str(start_time)+' and '+str(end_time))
    # Create the url that needs to access
    url = "http://api.openweathermap.org/data/2.5/history/city?id=4752046&APPID=5fbfc8b24f6c3c93a8ff66438c0639af&type=hour&start="+str(start_time)+"&end="+str(end_time)

    LOGGER.debug('The Url:\n\t'+url)
    # Open the url
    response = urllib.request.urlopen(url)

    # Read-in the JSON file and return the value
    json_text = response.read()
    return json_text


def write_json_to_file(filename, json_text):
    """
        Writes a string containing encoded JSON data to a JSON file.

        Parameters:
            filename:   Output JSON file to write.
            json_text:  String containing encoded JSON Data.

        No Return Values.

    """
    # writes json_text to a file
    LOGGER.debug('Writing json_text to file '+filename)
    temp_file = open(filename, 'w')
    try:
        json_text = str(json_text)
        json_text = json_text[2:len(json_text)]
        json_text = json_text[0:len(json_text)-3]
        temp_file.write(json_text)
    except Exception:
        LOGGER.warning('Error writing to file')
        raise

    temp_file.close()
    LOGGER.debug('Successfully wrote to file')
    return True
