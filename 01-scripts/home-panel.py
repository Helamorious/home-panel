from time import time
from time import sleep

from gpiozero import MotionSensor

import paho.mqtt.client as mqtt

pir = MotionSensor(14)
ha_sensor = "homeassistant/sensor/pir"

last_update = time()
last_reset = last_update

mqtt_server = "mqtt.hilton.local"

def pir_motion_detected(channel):
    client.publish(sensor, pir.motion_detected)
    print(pir.motion_detected)
    print("Motion detected")
    print(channel)
    global last_reset

def on_mqtt_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

def on_mqtt_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_mqtt_connect
client.on_message = on_mqtt_message
client.connect(mqtt_server, 1883, 60)

pir.when_motion = pir_motion_detected

while True:
    if time() - last_update >= 10:
        print("Idle %d secs" % (time() - last_reset))
        last_update = time()
    sleep(0.02)