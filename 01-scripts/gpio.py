from gpiozero import MotionSensor

pir = MotionSensor(14)

def pir_change(sensor):
#    if pir.motion_detected: display_off()
#    client.publish(hostname+"/"+str(sensor.pin), str({"motion_detected":pir.motion_detected}))
    global last_reset
    last_reset = time()

pir.when_motion = pir_change
pir.when_no_motion = pir_change
