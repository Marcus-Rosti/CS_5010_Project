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

def option_1():
    """ Returns a string that does...
    """
    return "write your own function!"

def option_2():
    """ Returns a string that does...
    """
    return "write your own function!"

def option_3():
    """ Returns a string that does...
    """
    return "write your own function!"

def option_4():
    """ Returns a string that does...
    """
    return "write your own function!"

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

#TEST TODO REMOVE
start_up("../data/SampleCSV.csv")
print(WEATHER_DATA)
