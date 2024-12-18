import os
import time
from pathlib import Path
import pyautogui

from config.data_reader import DataReader

from pages.File_Upload_Page import FileUploadPage
from pywinauto import Application

from utilities.PyAutoGuiUtils import PyAuto

relative_path = "file_upload/task_file.txt"
file_path = os.path.join(os.getcwd(), relative_path).replace("/", "\\")
EXPECTED_RESULT = "File Uploaded!"

home_dir = Path.home()
file_win = os.path.join(home_dir, "Desktop", "folder")
file_name = os.path.basename(relative_path)

FILE_X = 1192
FILE_Y = 400
DROP_X = 635
DROP_Y = 563
DURATION = 1


def test_file(driver, config_reader):
    url = config_reader.get_data_key("URL-11")
    driver.get(url)
    file_upload = FileUploadPage(driver)
    file_upload.send_file(file_path)
    text_upload = file_upload.text_upload.get_text()
    assert text_upload == EXPECTED_RESULT, f"Actual result:{text_upload}\nExpected result:{EXPECTED_RESULT}"
    text_file = file_upload.text_file.get_text()
    assert text_file == file_name


def test_file_and_dialog_window(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-11"))
    file_upload = FileUploadPage(driver)
    elem = file_upload.wait_drop_windows()
    file_upload.actions.move_to_element(elem).click().perform()
    time.sleep(1)
    file_upload.move_file(file_path)


def test_drag_drop_win(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-11"))
    file_upload = FileUploadPage(driver)
    pyauto = PyAuto()
    app = Application(backend="uia").start(f"explorer.exe {file_win}")
    time.sleep(2)
    pyauto.drag_and_drop_file(FILE_X, FILE_Y, DROP_X, DROP_Y, DURATION)
    file_upload.wait_text_drag_drop()
    text = file_upload.text_drag_drop.get_text()
    pyauto.close_window()
