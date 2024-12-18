from config.data_reader import DataReader
from pages.Basic_Authorization_Page import BasicAuthorizationPage

from faker import Faker

json_config = DataReader(DataReader.FILE_CONFIG)
fake = Faker()
random_value = str(fake.random_int(min=1, max=10))
USERNAME = "admin"
PASSWORD = "admin"
URL = f"http://{USERNAME}:{PASSWORD}@{json_config.get_data_key("URL-1")}"
EXPECTED_RESULT = "Congratulations! You must have the proper credentials."


def test_login_alert(driver):
    driver.get(URL)
    bap = BasicAuthorizationPage(driver)

    text = bap.text_congratulations.get_text()
    assert text == {EXPECTED_RESULT}, f"Actual result:{text}\nExpected result:{EXPECTED_RESULT}"
