import logging
import BOB

def main():
    logging.basicConfig(format='%(asctime)s:%(message)s',filename='logs.log', level=logging.DEBUG)
    logging.info('Started')
    BOB.do_something()
    logging.info('Finished')
    
if __name__ == '__main__':
    main()
