import os
import time

import pyautogui
from selenium.webdriver import ActionChains

from config.data_reader import DataReader

from pages.task12 import FileUpload
from pywinauto import Application

json_config = DataReader(DataReader.FILE_CONFIG)
relative_path = "file_upload/task_file.txt"
file_path = os.path.join(os.getcwd(), relative_path).replace("/", "\\")
file_win = "C:\\Users\\valeriy.kaurov\\Desktop\\folder"

file_name = os.path.basename(relative_path)


def test_file(driver):
    driver.get(json_config.get_data_key("URL-11"))
    file_upload = FileUpload(driver)
    file_upload.send_file(file_path)
    text_upload = file_upload.text_upload.get_text()
    assert text_upload == "File Uploaded!", f"Actual result:{text_upload}\nExpected result:File Uploaded"
    text_file = file_upload.text_file.get_text()
    assert text_file == file_name


def test_file_and_dialog_window(driver):
    driver.get(json_config.get_data_key("URL-11"))
    file_upload = FileUpload(driver)
    actions = ActionChains(driver)
    elem = file_upload.drag_drop_windows()
    actions.move_to_element(elem).click().perform()
    time.sleep(1)
    pyautogui.write(file_path)
    pyautogui.press('enter')
    file_upload.find_text_drag_drop()


def test_drag_drop_win(driver):
    driver.get(json_config.get_data_key("URL-11"))
    file_upload = FileUpload(driver)
    app = Application(backend="uia").start(f"explorer.exe {file_win}")
    time.sleep(2)

    file_x, file_y = 1192, 400

    drop_x, drop_y = 635, 563

    pyautogui.moveTo(file_x, file_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(drop_x, drop_y, duration=1)
    pyautogui.mouseUp()
    file_upload.find_text_drag_drop()
    text = file_upload.text_drag_drop.get_text()
    pyautogui.hotkey("alt", "f4")
