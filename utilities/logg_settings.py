import logging


class Logg:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('test.log', encoding='utf-8', mode="w")
    formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                                  datefmt='%d/%m/%Y %I:%M:%S')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
