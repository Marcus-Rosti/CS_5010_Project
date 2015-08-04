#import common_lib.py
import logging
import common_lib

#intialize logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/controller.log',level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def main():
    logger.debug('setting filename to ../data/testOutput.csv')
    # files to use
    sample_csv = '../data/SampleCSV.csv'
    output_json = '../data/live_example.json'
    output_csv =  '../data/SampleCSV.csv'

    (start_time, end_time) = common_lib.update(sample_csv)
    logger.debug('recieved times from date function')

    extracted_json = common_lib.extractor(start_time, end_time)
    logger.debug('received json from extract funciton')

    common_lib.write_json_to_file(output_json,extracted_json)

    common_lib.parseJSONFile(output_json,output_csv)
    logger.debug('csv was successfully updated')

if __name__ == "__main__":
    logger.info('\n\n\n\n\n\n')
    logger.info('Running controller with default inputs')
    main()
