import time

from config.data_reader import DataReader

from pages.task8 import IFrame

json_config = DataReader(DataReader.FILE_CONFIG)


def test_iframe(driver):
    driver.get(json_config.get_data_key("URL-8"))
    iframe = IFrame(driver)
    iframe.click_main_card()

    iframe.click_nested_frames_card()
    elem_1 = iframe.find_nested_frame_1()
    driver.switch_iframe(elem_1)
    text_parent = iframe.text_parent.get_text()
    assert text_parent == "Parent frame"

    elem_2 = iframe.find_nested_frame_2()
    driver.switch_iframe(elem_2)
    text_child = iframe.text_child.get_text()
    assert text_child == "Child Iframe"

    driver.switch_default()
    iframe.check_frames()
    elem_1 = iframe.find_frame_1()
    driver.switch_iframe(elem_1)
    text_frame1 = iframe.text1_frame.get_text()
    driver.switch_default()
    elem_2 = iframe.find_frame_2()
    driver.switch_iframe(elem_2)
    text_frame2 = iframe.text1_frame.get_text()
    assert text_frame1 == text_frame2
