from gpiozero import MotionSensor

pir = MotionSensor(14)

while True:
    pir.wait_for_motion()
    print("Movement detected")
    pir.wait_for_no_motion()
