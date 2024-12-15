import logging


class Logg:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    FILENAME = 'test.log'
    ENCODING = 'utf-8'
    FILEMODE = 'w'
    FORMAT = '%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]'
    DATE_FRMT = '%d/%m/%Y %I:%M:%S'

    handler = logging.FileHandler(FILENAME,
                                  encoding=ENCODING,
                                  mode=FILEMODE)
    formatter = logging.Formatter(FORMAT,
                                  datefmt=DATE_FRMT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
