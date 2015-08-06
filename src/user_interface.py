""" Displays and genereates the user interface

    To run this file:
        python user_interface.py
"""

import user_interface_lib as uil
import controller

LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/user_interface.log', level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

print_menu():
    print("MENU!!!!!!")

main():
    LOGGER.debug("Running main")
    uil.start_up("../SampleCSV.csv")
    print_menu():

if "__name__" == "main":
    main()
