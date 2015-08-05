""" Controller for updating weather data

    To run this file, use
        $ python controller.py
    From there if everything is formatted correctly, it should update the file
        correctly.  Next steps will be to take a file in as a command line
        parameter.  Pretty simple.

    Logs print to $Project_home/logs/controller.log
"""

#import common_lib.py
import logging
import common_lib

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
    file = "../data/"

def main():
    """ when controller.py is run, sends results to the empty
    """
    run_update_process("../data/SampleCSV.csv")


if __name__ == "__main__":
    LOGGER.info('\n\n\n\n\n\n')
    LOGGER.info('Running controller with default inputs')
    main()
