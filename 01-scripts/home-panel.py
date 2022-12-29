from gpiozero import MotionSensor

pir = MotionSensor(14)

def motion_detected():
    print("Motion detected")

pir.when_motion = motion_detected