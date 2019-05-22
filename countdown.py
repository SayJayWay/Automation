#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 60
while timeLeft > 0 :
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the coundown, play a sound file.
subprocess.Popen(['start', 'alarm.wave'], shell=True) # Can change alarm file to whatever

