""" The controller for user_interface

    This is a library of functions that will be used by user_interface

    This file should not be run
"""

import controller

LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/user_interface.log', level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

weather_data_frame = ''

def start_up(data_file):
""" Sets up data frame

    start_up takes in a datafile and spits out a global data frame that
        each of the subfunctions will use
"""
    controller.run_update_process(filename)
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
