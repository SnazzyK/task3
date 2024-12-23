import time

import pyautogui
from pywinauto import Application


class PyAuto:

    @staticmethod
    def drag_and_drop_file(file_x, file_y, drop_x, drop_y, duration,file_win):
        app = Application(backend="uia").start(f"explorer.exe {file_win}")
        time.sleep(2)
        pyautogui.moveTo(file_x, file_y)
        pyautogui.mouseDown()
        pyautogui.moveTo(drop_x, drop_y, duration)
        pyautogui.mouseUp()

    @staticmethod
    def close_window():
        pyautogui.hotkey("alt", "f4")

    @staticmethod
    def click_button_and_move_file(file_path):
        time.sleep(1)
        pyautogui.write(file_path)
        pyautogui.press('enter')
