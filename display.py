#!/usr/bin/env python
 
import sys
import time
import RPi.GPIO as io
import subprocess
from subprocess import call
 
io.setmode(io.BCM)
SHUTOFF_DELAY = 120  # seconds
PIR_PIN = 17         # Pin 11 on the board - change this to where you have your pir connected if different.
 
io.setup(PIR_PIN, io.IN)
turned_off = True
last_motion_time = time.time()

time.sleep(30)

while True:
    if io.input(PIR_PIN):
        last_motion_time = time.time()
        if turned_off:
            turned_off = False
            call(["/usr/bin/vcgencmd","display_power","1"])
    elif not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
        turned_off = True
        call(["/usr/bin/vcgencmd","display_power","0"])
    time.sleep(1)
