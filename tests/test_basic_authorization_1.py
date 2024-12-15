from config.data_reader import DataReader
from pages.task1 import BasicAuthorization

from faker import Faker

json_config = DataReader(DataReader.FILE_CONFIG)
fake = Faker()
random_value = str(fake.random_int(min=1, max=10))
USERNAME = "admin"
PASSWORD = "admin"


def test_login_alert(driver):
    driver.get(json_config.get_data_key("URL-1"))
    bap = BasicAuthorization(driver)
    bap.login(USERNAME, PASSWORD)
    text = bap.text_congratulations.get_text()
    assert text == "Congratulations! You must have the proper credentials.", f"Actual result:{text}\nExpected result:Congratulations! You must have the proper credentials."
