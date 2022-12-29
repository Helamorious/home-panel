from time import time
from time import sleep

from gpiozero import MotionSensor

pir = MotionSensor(14)

last_update = time()
last_reset = last_update

def motion_detected(channel):
    print(pir.motion_detected)
    print("Motion detected")
    print(channel)
    global last_reset

pir.when_motion = motion_detected

while True:
    if time() - last_update >= 10:
        print("Idle %d secs" % (time() - last_reset))
        last_update = time()
    sleep(0.02)