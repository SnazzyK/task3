from config.data_reader import DataReader

from pages.task11 import Scroll

from utilities.browser import Browser

json_config = DataReader(DataReader.FILE_CONFIG)
COUNT = 23


def test_scroll(driver):
    driver.get(json_config.get_data_key("URL-10"))
    scroll = Scroll(driver)

    while True:
        elem = scroll.found_elements()
        count_elem = len(elem)

        if count_elem == COUNT:
            print(count_elem)
            break
        else:
            Browser.scroll(0, 10000)
            scroll.found_elements()
