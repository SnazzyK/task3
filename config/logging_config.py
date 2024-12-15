import logging

from config.data_reader import DataReader

logger_config = DataReader(DataReader.LOGGER_CONFIG)


class Logger:

    @staticmethod
    def configure_logger():
        logging.basicConfig(level=logger_config.get_data_key("LEVEL"),
                            filename=logger_config.get_data_key("FILENAME"),
                            format=logger_config.get_data_key("FORMAT"),
                            datefmt=logger_config.get_data_key("DATEFMT"),
                            encoding=logger_config.get_data_key("ENCODING"),
                            filemode=logger_config.get_data_key("FILEMODE"))
