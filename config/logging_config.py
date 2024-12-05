import logging


class Logger:

    @staticmethod
    def configure_logger():
        logging.basicConfig(level=logging.DEBUG, filename='logging.log',
                            format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                            datefmt='%d/%m/%Y %I:%M:%S',
                            encoding='utf-8', filemode='w')
