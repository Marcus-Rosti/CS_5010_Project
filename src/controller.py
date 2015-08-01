import common_lib.py
import logging

logging.basicConfig(filename='../logs/controller.log',level=logging.DEBUG)

if __name__ == "__main__":
    main()
def main()
    logging.debug('setting filename to ../data/example.csv')
    filename = "../data/example.csv"

    dates = common_lib.update(filename))
    logging.debug('recieved dates from date function')
    
    extracted_json = common_lib.extract(dates)
    loggin.debug('received dates from extract funciton')
    
    common_lib.update_csv(extracted_json)
    logging.debut('csv was successfully updated')

