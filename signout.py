import time
import pyautogui
timer = input("Enter time until the signout happens:")
import win32gui, win32con
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
timer = float(timer)
time.sleep(timer)
pyautogui.hotkey("win", "m")
pyautogui.hotkey("alt", "f4")
pyautogui.press(["up", "up"])
pyautogui.press("enter")
#sometimes it doesnt register the first alt+f4
pyautogui.hotkey("win", "m")
pyautogui.hotkey("alt", "f4")
pyautogui.press(["up", "up"])
pyautogui.press("enter")
