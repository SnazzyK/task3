from config.data_reader import DataReader
from pages.task10 import DynamicContent

from utilities.browser import Browser

json_config = DataReader(DataReader.FILE_CONFIG)


def test_img(driver):
    driver.get(json_config.get_data_key("URL-9"))
    dc = DynamicContent(driver)

    while True:

        image_sources = dc.get_image_sources()

        if dc.has_matching_images(image_sources):
            break
        else:
            Browser.refresh()
