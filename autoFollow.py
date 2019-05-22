#1 python3
# autoFollow.py - Automatically follows between 90-110 followers on instagram
# Make sure that screen is at 250%

import pyautogui, time, random



# print(clickLocations)
 
for i in range(0,10):
    clickLocations = list(pyautogui.locateAllOnScreen('follow.jpg'))
    randNum = random.randint(5,25);
    clickInterval = randNum / 5;
    if clickLocations != '':
        for j in range(len(clickLocations)):
            clickCenter = pyautogui.center(clickLocations[j])
            # print(clickCenter)
            pyautogui.click(clickCenter)
            time.sleep(clickInterval)
    pyautogui.scroll(-5250)
    
