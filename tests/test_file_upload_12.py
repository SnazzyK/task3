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

home_dir = os.path.expanduser("~")
file_win = os.path.join(home_dir, "Desktop", "folder")
file_name = os.path.basename(relative_path)

FILE_X = 1192
FILE_Y = 400
DROP_X = 635
DROP_Y = 563
DURATION = 1


def test_file(driver):
    url = json_config.get_data_key("URL-11")
    driver.get(url)
    file_upload = FileUpload(driver)
    file_upload.send_file(file_path)
    text_upload = file_upload.text_upload.get_text()
    assert text_upload == "File Uploaded!", f"Actual result:{text_upload}\nExpected result:File Uploaded"
    text_file = file_upload.text_file.get_text()
    assert text_file == file_name


def test_file_and_dialog_window(driver):
    driver.get(json_config.get_data_key("URL-11"))
    file_upload = FileUpload(driver)
    elem = file_upload.wait_drop_windows()
    file_upload.actions.move_to_element(elem).click().perform()
    time.sleep(1)
    file_upload.file_move(file_path)


def test_drag_drop_win(driver):
    driver.get(json_config.get_data_key("URL-11"))
    file_upload = FileUpload(driver)
    app = Application(backend="uia").start(f"explorer.exe {file_win}")
    time.sleep(2)
    file_upload.drag_and_drop_file(FILE_X, FILE_Y, DROP_X, DROP_Y, DURATION)
    file_upload.find_text_drag_drop()
    text = file_upload.text_drag_drop.get_text()
    pyautogui.hotkey("alt", "f4")
