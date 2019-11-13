import logging
#fichier de logs

logging.basicConfig(filename='logs.log',level=logging.INFO)
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')


def do_something():
    logging.info('Doing something')
