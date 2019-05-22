import pyautogui, time
time.sleep(1)
pyautogui.click()   # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.01)    # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.01)    # move down
    pyautogui.dragRel(-distance, 0, duration=0.01)   # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.01)   # move up
