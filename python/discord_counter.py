import pyautogui
import time

time.sleep(3)

start = 69  # start amount
nums = 51   # amount of numbers to write
message_len = 20  # lenght of message    


for i in range(start + 1, start + nums, message_len):
    for j in range(i, min(i + message_len, start + nums)):
        pyautogui.typewrite(str(j))
        if j != min(i + message_len, start + nums) - 1:
            pyautogui.keyDown("shift")
            pyautogui.press("enter")
            pyautogui.keyUp("shift")
    pyautogui.press("enter")
    time.sleep(0.2)

