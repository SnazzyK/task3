from config.data_reader import DataReader

from pages.Hovers_Page import HoversPage

NAME_HOVER_1 = "name: user1"
NAME_HOVER_2 = "name: user2"
NAME_HOVER_3 = "name: user3"


def test_hover(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-5"))
    hover = HoversPage(driver)

    hover.check_hover(1)
    text_hover_1 = hover.get_text_element(1).get_text()
    assert text_hover_1 == NAME_HOVER_1, f"Actual result:{text_hover_1}\nExpected result:{NAME_HOVER_1}"

    hover.check_hover(2)
    text_hover_2 = hover.get_text_element(2).get_text()
    assert text_hover_2 == NAME_HOVER_2, f"Actual result:{text_hover_2}\nExpected result:{NAME_HOVER_2}"

    hover.check_hover(3)
    text_hover_3 = hover.get_text_element(3).get_text()
    assert text_hover_3 == NAME_HOVER_3, f"Actual result:{text_hover_3}\nExpected result:{NAME_HOVER_3}"
