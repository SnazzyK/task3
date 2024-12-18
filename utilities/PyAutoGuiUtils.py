import pyautogui


class PyAuto:

    @staticmethod
    def drag_and_drop_file(file_x, file_y, drop_x, drop_y, duration):
        pyautogui.moveTo(file_x, file_y)
        pyautogui.mouseDown()
        pyautogui.moveTo(drop_x, drop_y, duration)
        pyautogui.mouseUp()

    @staticmethod
    def close_window():
        pyautogui.hotkey("alt", "f4")
