#import common_lib.py
import logging
import common_lib

#intialize logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='../logs/controller.log',level=logging.DEBUG, \
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    
def main():
    logger.debug('setting filename to ../data/testOutput.csv')
    filename = "../data/testOutput.csv"

    dates = common_lib.update(filename)
    logger.debug(dates)
    logger.debug('recieved dates from date function')

#    extracted_json = common_lib.extract(dates)
    logger.debug('received dates from extract funciton')

    common_lib.parseJSONFile('../data/example.json')
    logger.debug('csv was successfully updated')

if __name__ == "__main__":
        main()
