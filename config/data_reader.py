import json
from utilities.logg_settings import Logg


class DataReader:
    FILE_CONFIG = "config/config.json"
    LOGGER_CONFIG = "config/logger_config.json"

    def __init__(self, file_config=FILE_CONFIG):
        self.file_path = file_config
        self.data = self.load_json_data()

    def load_json_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def get_data_key(self, key):
        return self.data[key]

    def get_data(self, key, index=None):

        value = self.data.get(key)

        if isinstance(value, dict):
            Logg.logger.debug(f"Key '{key}' is a dictionary. Returning values as a list.")
            return list(value.values())

        elif isinstance(value, list):
            Logg.logger.debug(f"Key '{key}' is a list. Returning the full list.")
            if index is not None:
                return value[index]

        elif isinstance(value, str):
            Logg.logger.debug(f"Key '{key}' is a string. Returning the string value.")
            return value
