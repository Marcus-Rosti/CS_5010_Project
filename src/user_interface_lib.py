""" The controller for user_interface

    This is a library of functions that will be used by user_interface

    List of Methods:
        unix_to_datetime(n) - takes a unix time and turns it into time and date.
        unix_to_date(n) - takes a unix time and turns it into a date only.
        date_to_unix(s) - takes a date and turns it into unix time
        kelvin_to_fahrenheit(t) - converts a kelvin temperature to fahrenheit.
        fahrenheit_to_kelvin(t) - converts a farhenheit temperature to kelvin.

    This file should not be run
"""

import controller
import logging
import datetime
import calendar
import pandas as pd
import time

LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/user_interface.log', level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


WEATHER_DATA = None

def start_up(data_file):
    """ Sets up data frame
        start_up takes in a datafile and spits out a global data frame that
            each of the subfunctions will use
    """

    LOGGER.debug("Updating data file with latest values.")
    controller.run_update_process(data_file)
    LOGGER.debug("Update complete");

    LOGGER.debug("Reading data file into Pandas Data Frame")
    try:
        global WEATHER_DATA
        WEATHER_DATA = pd.read_csv(data_file)
        WEATHER_DATA['datetime_std'] = WEATHER_DATA['date_unix'].apply(unix_to_datetime)
        WEATHER_DATA['date_std'] = WEATHER_DATA['date_unix'].apply(unix_to_date)
        WEATHER_DATA['main_temp_F'] = WEATHER_DATA['main_temp'].apply(kelvin_to_fahrenheit)
        WEATHER_DATA['main_temp_min_F'] = WEATHER_DATA['main_temp_min'].apply(kelvin_to_fahrenheit)
        WEATHER_DATA['main_temp_max_F'] = WEATHER_DATA['main_temp_max'].apply(kelvin_to_fahrenheit)
        LOGGER.debug("Data Frame created")
    except:
        return False
    return True

def today_weather():
    """ Returns a string that does contain most up-to-date weather information
    """

    # Read in required variables
    time = []
    [time.append(WEATHER_DATA['date_unix'][t]) for t in range(len(WEATHER_DATA['date_unix']))]
    ave_temp = []
    [ave_temp.append(WEATHER_DATA['main_temp'][t]) for t in range(len(WEATHER_DATA['main_temp']))]
    ave_pressure = []
    [ave_pressure.append(WEATHER_DATA['main_pressure'][t]) for t in range(len(WEATHER_DATA['main_pressure']))]
    ave_humidity = []
    [ave_humidity.append(WEATHER_DATA['main_humidity'][t]) for t in range(len(WEATHER_DATA['main_humidity']))]
    min_temp = []
    [min_temp.append(WEATHER_DATA['main_temp_min'][t]) for t in range(len(WEATHER_DATA['main_temp_min']))]
    max_temp = []
    [max_temp.append(WEATHER_DATA['main_temp_max'][t]) for t in range(len(WEATHER_DATA['main_temp_max']))]
    wind_speed = []
    [wind_speed.append(WEATHER_DATA['wind_speed'][t]) for t in range(len(WEATHER_DATA['wind_speed']))]
    ave_clouds = []
    [ave_clouds.append(WEATHER_DATA['clouds'][t]) for t in range(len(WEATHER_DATA['clouds']))]

    # Find the latest time
    last_time = unix_to_datetime(time[-1])

    # Calculate the average temperature for today
    n = s = 0
    for i in range(len(ave_temp)):
        n += 1
        s += ave_temp[i]

    ave_day_temp = kelvin_to_fahrenheit(s/n) # calculate the average temperature and convert to fahrenheit
    ave_day_temp = '%.2f' % ave_day_temp # convert to a string with two decimal places

    # Find the minimum temperature of the day
    n = min = 0
    for i in range(len(min_temp)):
        if min > min_temp[i]:
            min = min_temp[i]

    min_day_temp = kelvin_to_fahrenheit(min) # convert the minimum temperature to fahrenheit
    min_day_temp = '%.2f' % min_day_temp # convert to a string with two decimal places

    # Find the maximum temperature of the day
    n = max = 0
    for i in range(len(max_temp)):
        if max < max_temp[i]:
            max = max_temp[i]

    max_day_temp = kelvin_to_fahrenheit(max) # convert the maximum temperature to fahrenheit
    max_day_temp = '%.2f' % max_day_temp # convert to a string with two decimal places

    # Calculate the average pressure for today
    n = s = 0
    for i in range(len(ave_pressure)):
        n += 1
        s += ave_pressure[i]

    ave_day_pressure = s/n # calculate the average pressure
    ave_day_pressure = '%.2f' % ave_day_pressure # convert to a string with two decimal places

    # Calculate the average humidity for today
    n = s = 0
    for i in range(len(ave_humidity)):
        n += 1
        s += ave_humidity[i]

    ave_day_humidity = s/n # calculate the average humidity
    ave_day_humidity = '%.2f' % ave_day_humidity # convert to a string with two decimal places

    # Calculate the average wind speed for today
    n = s = 0
    for i in range(len(wind_speed)):
        n += 1
        s += wind_speed[i]

    ave_day_wind_speed = s/n # calculate the average wind speed
    ave_day_wind_speed = '%.2f' % ave_day_wind_speed # convert to a string with two decimal places

     # Calculate the average cloud coverage for today
    n = s = 0
    for i in range(len(ave_clouds)):
        n += 1
        s += ave_clouds[i]

    ave_day_clouds = s/n # calculate the average cloud coverage
    ave_day_clouds = '%.2f' % ave_day_clouds # convert to a string with two decimal places

    print_out = "Up to "+last_time+", the average temperature for today is "+ave_day_temp
    print_out = print_out +", with a minimum temperature as "+min_day_temp+" and a maximum temperature as "+max_day_temp
    print_out = print_out +". The average pressure is "+ave_day_pressure+", average humidity is "+ave_day_humidity
    print_out = print_out +" the average wind speed is "+ave_day_wind_speed+", and the average cloud coverage for today is "
    print_out = print_out +ave_day_clouds+"%."

    return print_out


def option_2():
    """ Returns a string that does...
    """
    return "write your own function!"

def date_range():
    '''
    Returns a string stating the range of dates of which we have weather data
    '''
    times = []
    #Read in file
    [times.append(WEATHER_DATA['date_unix'][t]) for t in range(len(WEATHER_DATA['date_unix']))]

    #catch an empty file
    if times == []:
        return "Error: No values read in"

    times.sort()
    oldest = unix_to_datetime(times[0])
    newest = unix_to_datetime(times[-1])

    return "The weather data ranges from "+oldest+" to "+newest+"."

def ave_temps():
    '''
    Returns a string containing the month's average temperature and the
    average temperature from the previous week.
    '''
    #Create a list of time and temperature data
    temps = []
    [temps.append([WEATHER_DATA['date_unix'][t], WEATHER_DATA['main_temp'][t]]) for t in range(len(WEATHER_DATA['date_unix']))]

    #convert to fahrenhiet
    for i in range(len(temps)):
        temps[i][1] = kelvin_to_fahrenheit(temps[i][1])

    week = 7*24*3600 #Number of seconds in a week
    week = int(time.time() - week) #A week ago

    #Average the temps that greater than week
    n = s = 0
    for i in range(len(temps)):
        if temps[i][0] <= week:
            n += 1
            s += temps[i][1]
    if n == 0:
        return "Please update the data"
    wtemp = s/n
    wtemp = '%.2f' % wtemp #Convert to a string with two decimal places

    #convert date to m/d/y format
    for i in range(len(temps)):
        temps[i][0] = unix_to_date(temps[i][0])

    #get the current month
    month = unix_to_date(time.time())[:2]

    #find and average the temperatures in the same month
    n = s = 0
    for i in range(len(temps)):
        if month == temps[i][0][:2]:
            n += 1
            s += temps[i][1]
    if n == 0:
        return "Please update and/or fill gaps in the data"
    mtemp = s/n
    mtemp = '%.2f' % mtemp #Convert to a string with two decimal places

    #Generate a name for the month
    if month == '01':
        name = "January"
    elif month == '02':
        name = "February"
    elif month == '03':
        name = "March"
    elif month == '04':
        name = "April"
    elif month == '05':
        name = "May"
    elif month == '06':
        name = "June"
    elif month == '07':
        name = 'July'
    elif month == "08":
        name = 'August'
    elif month == '09':
        name = "September"
    elif month == '10':
        name = "October"
    elif month == '11':
        name = "November"
    elif month == '12':
        name = "December"
    else:
        return "Month name error"

    #Print out temperatures
    return "The average temperature for "+name+" is "+mtemp+" F.  The average temperature this past week was "+wtemp+" F."

def unix_to_datetime(n):
    '''
    Takes in unix date as an integer and returns date and time as a string

    Parameters: n - unix timestamp as an integer

    Returns: A string in the format m/d/y h:m:s
    '''
    return datetime.datetime.fromtimestamp(n).strftime('%m/%d/%Y %H:%M:%S')

def unix_to_date(n):
    '''
    Takes in unix date as an integer, and returns just the date as a string

    Parameters: n - unix timestamp as an integer

    Returns: A string in the format m/d/y
    '''
    return datetime.datetime.fromtimestamp(n).strftime('%m/%d/%Y')

def date_to_unix(s):
    '''
    Takes in date and returns unix date as an integer

    Parameters: s -  The date as a sting in m/d/y format

    Returns: Unix timestamp as an integer
    '''
    d = datetime.datetime.strptime(s, '%m/%d/%Y')
    return calendar.timegm(d.timetuple())

def kelvin_to_fahrenheit(t):
    '''
    Converts kelvin to fahrenheit

    Parameters: t - Kelvin temperature as an integer

    Returns: Farhernheit temperature as an integer
    '''
    return 1.8*(t-273)+32

def fahrenheit_to_kelvin(t):
    '''
    Converts fahrenheit to kelvin

    Parameters: t - Farhernheit temperature as an integer

    Results: Kelvin temperature as an integer
    '''
    return (t-32)/1.8 + 273
