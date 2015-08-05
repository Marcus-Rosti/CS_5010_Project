#import common_lib.py
import logging
import common_lib

#intialize logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/controller.log',level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def run_update_process(update_file):
    logger.debug('setting filename to ../data/testOutput.csv')
    # files to use
    output_json = '../data/temp_example.json'

    (start_time, end_time) = common_lib.update(update_file)
    logger.debug('recieved times from date function')
    if(start_time == 0):
        logger.debug('No need to update')
        return

    extracted_json = common_lib.extractor(start_time, end_time)
    logger.debug('received json from extract funciton')

    common_lib.write_json_to_file(output_json,extracted_json)

    common_lib.parseJSONFile(output_json,update_file)
    logger.debug('csv was successfully updated')

def main():
    run_update_process("../data/SampleCSV.csv")


if __name__ == "__main__":
    logger.info('\n\n\n\n\n\n')
    logger.info('Running controller with default inputs')
    main()
