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
import matplotlib.pyplot as py
import numpy as np

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

def get_average(list):
    """ Helper function to calculate the average of a list
        Param: A list of numbers
        Returns: A single float or NAN depending on input
    """
    if len(list) > 0:
        return float(sum(list))/len(list)
    else:
        return float('nan')

def today_weather():
    """ Returns a string that does contain most up-to-date weather information for today
    """
    todays_weather = WEATHER_DATA[WEATHER_DATA['date_std'] == unix_to_date(time.time())]

    # Read in required variables
    times_today  = list(todays_weather['date_unix'].values)
    ave_temp     = list(todays_weather['main_temp'].values)
    ave_pressure = list(todays_weather['main_pressure'].values)
    ave_humidity = list(todays_weather['main_humidity'].values)
    min_temp     = list(todays_weather['main_temp_min'].values)
    max_temp     = list(todays_weather['main_temp_max'].values)
    wind_speed   = list(todays_weather['wind_speed'].values)
    ave_clouds   = list(todays_weather['clouds'].values)

    # Find the latest time
    last_time = unix_to_datetime(times_today[-1])

    # Calculate the average temperature for today
    ave_day_temp = '%.2f' % kelvin_to_fahrenheit(get_average(ave_temp)) # calculate the average temperature and convert to fahrenheit

    # Find the minimum temperature of the day
    min = min_temp[0]
    for i in range(len(min_temp)):
        if min > min_temp[i]:
            min = min_temp[i]

    min_day_temp = '%.2f' % kelvin_to_fahrenheit(min) # convert the minimum temperature to fahrenheit

    # Find the maximum temperature of the day
    max = 0
    for i in range(len(max_temp)):
        if max < max_temp[i]:
            max = max_temp[i]

    max_day_temp = '%.2f' % kelvin_to_fahrenheit(max) # convert the maximum temperature to fahrenheit

    # Calculate the average pressure for today
    ave_day_pressure = '%.2f' % get_average(ave_pressure) # calculate the average pressure

    # Calculate the average humidity for today
    ave_day_humidity = '%.2f' % get_average(ave_humidity) # calculate the average humidity

    # Calculate the average wind speed for today
    ave_day_wind_speed = '%.2f' % get_average(wind_speed) # calculate the average wind speed

     # Calculate the average cloud coverage for today
    ave_day_clouds = '%.2f' % get_average(ave_clouds) # calculate the average cloud coverage

    print_out = "Up to "+last_time+", the average temperature for today is "+ave_day_temp
    print_out = print_out +"F, with a minimum temperature as "+min_day_temp+"F and a maximum temperature as "+max_day_temp
    print_out = print_out +"F. The average pressure is "+ave_day_pressure+"hPa, average humidity is "+ave_day_humidity
    print_out = print_out +"%, average wind speed is "+ave_day_wind_speed+"m/s, and the average cloud coverage for today is "
    print_out = print_out +ave_day_clouds+"%."

    return print_out


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

def temp_graph():
    '''
    outputs a line graph of temperatures per day
    '''
    #Select desired data
    temps = []
    [temps.append([WEATHER_DATA['date_unix'][t], WEATHER_DATA['main_temp_F'][t],
     WEATHER_DATA["main_pressure"][t], WEATHER_DATA['main_humidity'][t],
     WEATHER_DATA["clouds"][t]]) for t in range(len(WEATHER_DATA['date_unix']))]

    #Sort chronologically
    temps.sort()
    #Convert to m/d/y format
    for i in range(len(temps)):
        temps[i][0] = unix_to_date(temps[i][0])

    #Create average stats per day
    day = []
    temp = []
    humid = []
    cloud = []
    j = 0  #Keeps track of how many entries per day
    for i in range(len(temps)):
        if day == []: #initialize
            day.append(temps[i][0])
            temp.append(temps[i][1])
            humid.append(temps[i][3])
            cloud.append(temps[i][4])
            j += 1
        elif day[-1] == temps[i][0]: #Add in values for same day
            temp[-1] += temps[i][1]
            humid[-1] += temps[i][3]
            cloud[-1] += temps[i][4]
            j += 1
        else:  #Create a new day and average the previous
            temp[-1] = temp[-1]/j
            humid[-1] = humid[-1]/j
            cloud[-1] = cloud[-1]/j
            day.append(temps[i][0])
            temp.append(temps[i][1])
            humid.append(temps[i][3])
            cloud.append(temps[i][4])
            j = 1
    #average the last day
    temp[-1] = temp[-1]/j
    humid[-1] = humid[-1]/j
    cloud[-1] = cloud[-1]/j

    #Alter day to make readable
    for i in range(len(day)):
        if day[i][3:5] != '01':  #First of every month
            day[i] = ''

    #Create graph
    #py.plot(cloud, 'k', label='Cloud Coverage (%)')  Too busy with this value
    py.clf()
    py.plot(humid, 'b', label='Humidity (%)')
    py.plot(temp, 'r', label='Temperature (F)')
    py.legend(loc='best')
    py.title("Daily Statistics")
    py.xticks(np.arange(len(day)), day)
    py.xlabel("Date")
    py.show()


def weather_barchart():
    '''
    outputs a bar chart of the weather for the past 7 days
    '''
    # Select desired data
    week = 7*24*3600 #Number of seconds in a week
    week = int(time.time() - week) #A week ago
    week_weather = WEATHER_DATA[WEATHER_DATA['date_std'] >= unix_to_date(week)]

    # Read in required variables
    weather = pd.Series(list(week_weather['weather_main'].values))

    # Create a bar graph of different weather types
    py.clf()
    weather.value_counts().plot(kind = 'bar')
    py.show()

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
