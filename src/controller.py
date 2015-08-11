""" Controller for updating weather data

    To run this file, use
        $ python controller.py
    From there if everything is formatted correctly, it should update the file
        correctly.  Next steps will be to take a file in as a command line
        parameter.  Pretty simple.

    Logs print to $Project_home/logs/controller.log
"""

import logging
import common_lib
import time
import sys, getopt, os

#intialize logging
LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/controller.log', level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def run_update_process(update_file):
    """ Updates a csv of weather data

        Function takes in a file to update and appends data, if it's available
        The parameter should be a direct link to the file
    """
    (start_time, end_time) = common_lib.update(update_file)
    first_time = start_time
    start_time = 0
    counter = 1
    two_previous = previous = -1
    if end_time != 0:
        weight = (1-(first_time/end_time))

    while end_time != 0:
        LOGGER.debug("*******************\n\tUpdate :: "+str(counter))
        if(counter != 1):
            print("Updating: "+'%2.2f'%((1-(end_time-start_time)/end_time/weight)*100)+"%")
        counter = counter + 1
        two_previous = previous
        previous = start_time
        (start_time, end_time) = common_lib.update(update_file)

        if(two_previous == previous):
            LOGGER.debug('Hmmm, there\'s some error. The api failed.')
            print("WARNING: OpenWeather responded with nothing.")
            break

        LOGGER.debug('recieved times from date function')

        # files to use
        output_json = '../data/temp_example.json'
        if not os.path.exists(output_json):
            open(output_json, 'w').close()

        extracted_json = common_lib.extractor(start_time, end_time)
        LOGGER.debug('received json from extract funciton')

        common_lib.write_json_to_file(output_json, extracted_json)

        common_lib.parseJSONFile(output_json, update_file)
        os.remove(output_json) # remove this file, unneeded
    LOGGER.debug('csv was successfully updated')
    return True

def run_init_process():
    """ Initialize a file with appropriate headers

        This deals with the case of no file passed via clp
    """
    file = "../data/"+str(time.time())+"_data.csv"
    LOGGER.debug('Initializeing a new file: ' + file)
    empty_file = open(file, 'w')
    headers = "date_unix,main_temp,main_pressure,main_humidity,\
main_temp_min,main_temp_max,wind_speed,wind_deg,weather_main,\
weather_description,clouds\n"

    empty_file.write(headers)
    empty_file.close()

    return run_update_process(file)


def main(argv):
    """ Runs controller from the command line

        Takes a command line via argv

        The general usage here:
            python controller.py [-h] -i <inputfile>
        As far as I can tell, this handles errors quite well and will
            print out help if the user makes some sort of error in entry

        -i : required.  Takes a file location
    """
    LOGGER.debug('Taking command line parameters')
    infile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        LOGGER.debug('There\'s some error reading in command line')
        sys.exit()
        raise
    try:
        for opt, arg in opts:
            if opt == '-h':
                LOGGER.debug('Printing out help and exiting')
                print('python controller.py [-h] -i <inputfile>')
                sys.exit()
            elif opt == '-i':
                infile = arg
                LOGGER.debug('Using file: '+infile)
    except Exception:
        LOGGER.debug('Exiting!')
        raise

    if infile == '':
        LOGGER.debug('No inputfile, running init')
        run_init_process()
    else:
        run_update_process(infile)
    return 0


if __name__ == "__main__":
    LOGGER.info('\n\n\n\n\n\n')
    main(sys.argv[1:])
