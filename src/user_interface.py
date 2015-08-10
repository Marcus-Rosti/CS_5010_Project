""" Displays and genereates the user interface

    To run this file:
        python user_interface.py
"""

import user_interface_lib as uil
import logging
import sys

NUMBER_OF_OPTIONS = 5 # Number of options available

LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/user_interface.log', level=logging.DEBUG,\
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def print_breaks():
    """ Prints out line breaks

        Just so I'm consistent throughout without having to reuse code
    """
    print("#########################################")
    return True

def print_menu():
    """ Prints out thte menu options
    """
    LOGGER.debug('Printing menu')
    print_breaks()
    print("Select and option from below")
    print("\t1) Get today's weather")
    print("\t2) Option 2")
    print("\t3) Option 3")
    print("\t4) Get average temperatures")
    print("\t5) Get data range")
    print("\t0) Exit")
    print_breaks()
    return True

def accept_user_input():
    """ Deals with user input

        returns an int assciated to the menu

        if the value is out of range, then we'll return -1
    """
    user_selection = float("-inf")
    try:
        user_input = input('Make a selection: ')
        user_selection = int(user_input)
    except ValueError:
        LOGGER.error('User input error: '+str(user_selection))
        print("Please input a correct value")
        return -1
    if user_selection > NUMBER_OF_OPTIONS or user_selection < 0:
        LOGGER.error('User input error: '+str(user_selection))
        print('Please input a correct value')
        return -1
    print_breaks()
    return user_selection


def initalize_library():
    """ Calls the setup function
    """
    print_breaks()
    print('Initializing...')
    uil.start_up('../data/SampleCSV.csv')
    return True


def print_welcome():
    """ Prints my stupid welcome text
    """
    print(",--.   ,--.       ,--.")
    print("|  |   |  | ,---. |  | ,---. ,---. ,--,--,--. ,---. ")
    print("|  |.'.|  || .-. :|  || .--'| .-. ||        || .-. :")
    print("|   ,'.   |\   --.|  |\ `--.' '-' '|  |  |  |\   --.")
    print("'--'   '--' `----'`--' `---' `---' `--`--`--' `----'")
    print(",--------.")
    print("'--.  .--',---.")
    print("   |  |  | .-. |")
    print("   |  |  ' '-' '")
    print("   `--'   `---'")
    print(" ,-----.          ,--.,--.,--.")
    print("'  .--./,--.  ,--.`--'|  ||  | ,---.")
    print("|  |     \  `'  / ,--.|  ||  || .-. :")
    print("'  '--'\  \    /  |  ||  ||  |\   --.")
    print(" `-----'   `--'   `--'`--'`--' `----'")
    print(",--.   ,--.                 ,--.  ,--.")
    print("|  |   |  | ,---.  ,--,--.,-'  '-.|  ,---.  ,---. ,--.--.")
    print("|  |.'.|  || .-. :' ,-.  |'-.  .-'|  .-.  || .-. :|  .--'")
    print("|   ,'.   |\   --.\ '-'  |  |  |  |  | |  |\   --.|  |")
    print("'--'   '--' `----' `--`--'  `--'  `--' `--' `----'`--'")
    return True

def print_goodbye():
    """ Cleans up and exits
    """
    LOGGER.debug('Exiting classily')
    print("Stay classy, Charlottesville")
    print_breaks()
    sys.exit()

def deal_with_user_input(selection):
    """ Deals with input from stdin

        This is the workhorse. It proccesses user input via uil and then prints
            the resulting string.
    """
    output = 'Failure?'
    LOGGER.debug('User input: '+str(selection))
    if selection == 0:
        print_goodbye()
    elif selection == 1:
        print('Processing option ' + str(selection))
        output = uil.today_weather()
    elif selection == 2:
        print('Processing option ' + str(selection))
        # output = uil.option_2()
    elif selection == 3:
        print('Processing option ' + str(selection))
        # output = uil.option_3()
    elif selection == 4:
        print('Processing option ' + str(selection))
        output = uil.ave_temps()
    elif selection == 5:
        print('Processing option ' + str(selection))
        output = uil.date_range()
    else:
        LOGGER.debug('Definitely shouldn\'t have ended up here')
        sys.exit()
    print(output)
    print_breaks()
    return True


def main():
    """ Entry point for the command line interface
    """
    LOGGER.debug("Running main")
    print_welcome()
    initalize_library()
    selection = ''
    while True:
        print_menu()
        selection = accept_user_input()
        if selection == -1:
            continue
        deal_with_user_input(selection)


if __name__ == "__main__":
    LOGGER.info('\n\n\n\n\n\n')
    main()
