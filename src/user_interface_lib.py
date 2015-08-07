""" The controller for user_interface

    This is a library of functions that will be used by user_interface

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
    # Takes in unix date as an int, returns date and time as a string
    return datetime.datetime.fromtimestamp(n).strftime('%m/%d/%Y %H:%M:%S')
 
def unix_to_date(n):
    # Takes in unix date as an int, returns date as a string
    return datetime.datetime.fromtimestamp(n).strftime('%m/%d/%Y')
    
def date_to_unix(s):
    #Takes in date as a sting in m/d/y format and returns unix date as an int
    d = datetime.datetime.strptime(s, '%m/%d/%Y')
    return calendar.timegm(d.timetuple())
    
def kelvin_to_fahrenheit(t):
    #Converts kelvin to fahrenheit
    return 1.8*(t-273)+32
    
def fahrenheit_to_kelvin(t):
    #Converts fahrenheit to kelvin
    return (t-32)/1.8 + 273