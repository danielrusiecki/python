#!/usr/bin/env python
import pyautogui
import time

i = 0
print('Press Ctrl-C to quit.')
try:
      while True:
            time.sleep(15)
            i += 1
            print(str(i))
            time.sleep(15)
            i += 1
            print(str(i))
            time.sleep(15)
            i += 1
            print(str(i))
            time.sleep(13)
            pyautogui.moveTo(700, 400, duration=0.25)
            pyautogui.moveTo(800, 400, duration=0.25)
            pyautogui.moveTo(800, 500, duration=0.25)
            pyautogui.moveTo(700, 500, duration=0.25)
            pyautogui.click()
            pyautogui.typewrite('x')
            i += 1
            print(str(i) + '\n')
            #print('\n')
except KeyboardInterrupt:
      print('\nDone.')
