#!/usr/bin/env python3

from time import time
from time import sleep
import socket
import paho.mqtt.client as mqtt
import dpms
import subprocess
import threading
from gpiozero import MotionSensor

hostname = socket.gethostname()

pir = MotionSensor(14)
last_update = time()
last_reset = last_update

display = dpms.DPMS(":0")
display.SetTimeouts(30, 600, 3600)

mqtt_server = "mqtt.hilton.local"

def display_on():
    display.ForceLevel(dpms.DPMSModeOn)

def pir_change(sensor):
    if pir.motion_detected: display_on()
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