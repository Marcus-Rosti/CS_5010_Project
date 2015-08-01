#import common_lib.py
import logging

logging.basicConfig(filename='../logs/controller.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def main():
    logging.debug('setting filename to ../data/example.csv')
    filename = "../data/example.csv"

#    dates = common_lib.update(filename))
    logging.debug('recieved dates from date function')
    
#    extracted_json = common_lib.extract(dates)
    logging.debug('received dates from extract funciton')
    
#    common_lib.update_csv(extracted_json)
    logging.debug('csv was successfully updated')

if __name__ == "__main__":
        main()
