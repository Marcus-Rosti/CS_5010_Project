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
import sys, getopt

#intialize logging
LOGGER = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/controller.log', level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def run_update_process(update_file):
    """ Updates a csv of weather data

        Function takes in a file to update and appends data, if it's available
        The parameter should be a direct link to the file
    """
    LOGGER.debug('setting filename to ../data/testOutput.csv')
    # files to use
    output_json = '../data/temp_example.json'

    (start_time, end_time) = common_lib.update(update_file)
    LOGGER.debug('recieved times from date function')
    if end_time == 0:
        LOGGER.debug('No need to update')
        return

    extracted_json = common_lib.extractor(start_time, end_time)
    LOGGER.debug('received json from extract funciton')

    common_lib.write_json_to_file(output_json, extracted_json)

    common_lib.parseJSONFile(output_json, update_file)
    LOGGER.debug('csv was successfully updated')

def run_init_process():
    """ Initialize a file with appropriate headers

        This deals with the case of no file passed via clp
    """
    file = "../data/"+str(time.time())+"_data.csv"
    LOGGER.debug('Initializeing a new file: ' + file)
    f = open(file, 'w')
    headers = "date_unix, main_temp, main_pressure, main_humidity,\
     main_temp_min, main_temp_max, wind_speed, wind_deg, weather_main,\
     weather_description, clouds"
    f.write(headers)
    f.close()

    run_update_process(file)


def main(argv):
    """ when controller.py is run, sends results to the empty
    """
    LOGGER.debug('Taking command line parameters')
    infile = ''
    try:
        opts = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        print('controller.py <inputfile>')
        sys.exit(2)
    try:
        for arg in opts:
            if arg == '-h':
                print('test.py <inputfile>')
                sys.exit()
            else:
                infile = arg
    except:
        LOGGER.debug('There\'s something werid...')
        sys.exit()
    finally:
        if infile != '':
            LOGGER.debug('No inputfile, running init')
            run_init_process()
        else:
            run_update_process("../data/SampleCSV.csv")

    return 0


if __name__ == "__main__":
    LOGGER.info('\n\n\n\n\n\n')
    main(sys.argv[1:])
