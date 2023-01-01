import paho.mqtt.client as mqtt

mqtt_server = "mqtt.hilton.local"

def on_mqtt_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

def on_mqtt_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)):qw

client = mqtt.Client()
client.on_connect = on_mqtt_connect
client.on_message = on_mqtt_message
client.connect(mqtt_server, 1883, 60)
