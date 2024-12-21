import time

from config.data_reader import DataReader

from pages.iframe_page import IFramePage

EXPECTED_RESULT_PARENT = "Parent frame"
EXPECTED_RESULT_CHILD = "Child Iframe"
EXPECTED_RESULT_FRAME = "This is a sample page"


def test_iframe(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-8"))
    iframe = IFramePage(driver)
    iframe.wait_for_open()
    iframe.click_main_card()
    iframe.click_nested_frames_card()
    nested_iframe_1 = iframe.wait_nested_iframe_1()
    driver.switch_to_frame(nested_iframe_1)
    text_parent = iframe.text_parent.get_text()
    assert text_parent == EXPECTED_RESULT_PARENT, f"Actual result:{text_parent}\nExpected result:{EXPECTED_RESULT_PARENT}"

    nested_iframe_2 = iframe.wait_nested_iframe_2()
    driver.switch_to_frame(nested_iframe_2)
    text_child = iframe.text_child.get_text()
    assert text_child == EXPECTED_RESULT_CHILD, f"Actual result:{text_parent}\nExpected result:{EXPECTED_RESULT_CHILD}"

    driver.switch_default()
    iframe.click_frames()
    iframe_1 = iframe.wait_iframe_1()
    driver.switch_to_frame(iframe_1)
    text_frame1 = iframe.text1_frame.get_text()
    driver.switch_default()

    iframe_2 = iframe.wait_iframe_2()
    driver.switch_to_frame(iframe_2)
    text_frame2 = iframe.text1_frame.get_text()
    assert text_frame1 == text_frame2, f"Actual result:{text_frame1}\nExpected result:{EXPECTED_RESULT_FRAME}"
