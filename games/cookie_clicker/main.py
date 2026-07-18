import pyautogui
import sys


screen_width, screen_height = pyautogui.size()

px = 900
py = [400, 480, 560, 640, 720, 798, 880, 940, 1014]
pyautogui.PAUSE = 0.01
while True:
    pyautogui.moveTo(176, 653)  # cookie
    for i in range(1000):
        pyautogui.click(button="left")
    for item in py[::-1]:
        pyautogui.moveTo(px, item)
        pyautogui.click(button="left")
