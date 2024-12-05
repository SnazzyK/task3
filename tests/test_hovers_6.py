from config.data_reader import DataReader

from pages.task6 import Hovers

json_config = DataReader(DataReader.FILE_CONFIG)


def test_hover(driver):
    driver.get(json_config.get_data_key("URL-5"))
    hover = Hovers(driver)

    hover.check_hover_1()
    text_hover_1 = hover.text_1.get_text()
    assert text_hover_1 == "name: user1", f"Actual result:{text_hover_1}\nExpected result:name: user1"

    hover.check_hover_2()
    text_hover_2 = hover.text_2.get_text()
    assert text_hover_2 == "name: user2", f"Actual result:{text_hover_2}\nExpected result:name: user2"

    hover.check_hover_3()
    text_hover_3 = hover.text_3.get_text()
    assert text_hover_3 == "name: user3", f"Actual result:{text_hover_3}\nExpected result:name: user3"
