""" Displays and genereates the user interface

    To run this file:
        python user_interface.py
"""

import user_interface_lib as uil

LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/user_interface.log', level=logging.DEBUG,\
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def print_menu():
    print("MENU!!!!!!")

def main():
    LOGGER.debug("Running main")
    uil.start_up("../SampleCSV.csv")
    print_menu()

if __name__ == "__main__":
    LOGGER.info('\n\n\n\n\n\n')
    main()
