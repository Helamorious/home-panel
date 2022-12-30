from time import time
from time import sleep
import socket
import paho.mqtt.client as mqtt
import subprocess
from gpiozero import MotionSensor
from Xlib import display

hostname = socket.gethostname()

pir = MotionSensor(14)
last_update = time()
last_reset = last_update

mqtt_server = "mqtt.hilton.local"

disp = display.Display()

def wake_screen():
    subprocess.run(["xset", "-d", ":0", "s", "reset"])

def pir_change(sensor):
    if pir.motion_detected: wake_screen()
    client.publish(hostname+"/"+str(sensor.pin), str({"motion_detected":pir.motion_detected}))
    global last_reset
    last_reset = time()

def on_mqtt_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

def on_mqtt_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_mqtt_connect
client.on_message = on_mqtt_message
client.connect(mqtt_server, 1883, 60)

pir.when_motion = pir_change
pir.when_no_motion = pir_change

while True:
    if time() - last_update >= 10:
        print("Idle %d secs" % (time() - last_reset))
        last_update = time()
    sleep(0.02)