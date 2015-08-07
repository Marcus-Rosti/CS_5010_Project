""" The controller for user_interface

    This is a library of functions that will be used by user_interface

    This file should not be run
"""

import controller
import logging
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

