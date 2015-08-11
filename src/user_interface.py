""" Displays and genereates the user interface

    To run this file:
        python user_interface.py

    List of functions:
        print_breaks
        print_menu
        accept_user_input
        initalize_library
        print_welcome
        print_goodbye
        deal_with_user_input
        main
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

        Params:
            None
        Return:
            None
    """
    print("#########################################")
    return True

def print_menu():
    """ Prints out thte menu options

        Params:
            None
        Return:
            None
    """
    LOGGER.debug('Printing menu')
    print_breaks()
    print("Select and option from below")
    print("\t1) Get Today's Weather")
    print("\t2) Get Average Temperatures")
    print("\t3) Get Graphical Temperatures and Statistics")
    print("\t4) Get Weather Bar Chart for the Past 7 Days")
    print("\t5) Get Data Range")
    print("\t0) Exit")
    print_breaks()
    return True

def accept_user_input():
    """ Deals with user input

        returns an int assciated to the menu

        if the value is out of range, then we'll return -1

        Params:
            None
        Return:
            user_selection
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
    """ Calls the setup function from library

        Params:
            None
        Return:
            None
    """
    print_breaks()
    print('Initializing...')
    uil.start_up('../data/SampleCSV.csv')
    return True


def print_welcome():
    """ Prints my stupid welcome text

        Params:
            None
        Return:
            None
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

        Params:
            None
        Return:
            None
    """
    LOGGER.debug('Exiting classily')
    print("Stay classy, Charlottesville")
    print_breaks()
    sys.exit()

def deal_with_user_input(selection):
    """ Deals with input from stdin

        This is the workhorse. It proccesses user input via uil and then prints
            the resulting string.

        Params:
            Selection - Within the range of possible options
        Return:
            None
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
        output = uil.ave_temps()
    elif selection == 3:
        print('Processing option ' + str(selection))
        uil.temp_graph()
        output = "Temp graph"
    elif selection == 4:
        print('Processing option ' + str(selection))
        uil.weather_barchart()
        output = "Bar graph"
    elif selection == 5:
        print('Processing option ' + str(selection))
        output = uil.date_range()
    else:
        LOGGER.debug('Definitely shouldn\'t have ended up here')
        sys.exit()
    print_breaks()
    print(output)
    return True


def main():
    """ Entry point for the command line interface

        Params:
            None
        Return:
            None
    """
    LOGGER.debug("Running main")
    print_welcome()
    initalize_library()
    selection = ''
    while True:
        print_menu()
        try:
            selection = accept_user_input()
        except KeyboardInterrupt:
            LOGGER.debug('Handling KeyboardInterrupt')
            print('')
            print_goodbye()
        if selection == -1:
            continue
        deal_with_user_input(selection)


if __name__ == "__main__":
    LOGGER.info('\n\n\n\n\n\n')
    main()
