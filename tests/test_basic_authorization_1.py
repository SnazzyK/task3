from config.data_reader import DataReader
from pages.basic_authorization_page import BasicAuthorizationPage
from dotenv import load_dotenv
import os
from faker import Faker

json_config = DataReader(DataReader.FILE_CONFIG)
load_dotenv()
fake = Faker()
random_value = str(fake.random_int(min=1, max=10))
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
URL = f"http://{username}:{password}@{json_config.get_data_key("URL-1")}"
EXPECTED_RESULT = "Congratulations! You must have the proper credentials."


def test_login_alert(driver):
    driver.get(URL)
    bap = BasicAuthorizationPage(driver)
    bap.wait_for_open()

    text = bap.get_text_congratulations
    assert text == {EXPECTED_RESULT}, f"Actual result:{text}\nExpected result:{EXPECTED_RESULT}"
