from time import time
from time import sleep
from gpiozero import MotionSensor
from rpi_backlight import Backlight 

import socket
import paho.mqtt.client as mqtt

hostname = socket.gethostname()

display = Backlight()
display.fade_duration = 1
display.brightness = 60

pir = MotionSensor(14)
last_update = time()
last_reset = last_update

mqtt_server = "mqtt.hilton.local"

def display_off():
    display.power = False

def display_on():
    display.power = True

def pir_change(sensor):
    if pir.motion_detected: display_off()
    client.publish(hostname+"/"+str(sensor.pin), str({"motion_detected":pir.motion_detected}))
    global last_reset
    last_reset = time()

def on_mqtt_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

def on_mqtt_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)):qw

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