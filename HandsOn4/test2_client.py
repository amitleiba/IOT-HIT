import json
import time
from typing import Any

import paho.mqtt.client as mqtt

from mqtt_init import *

LAST_FOUR_DIGITS_OF_ID = 6819
SIGNATURE_NAME = "AL"
CLIENT_ID = f"Iot_{SIGNATURE_NAME}_{LAST_FOUR_DIGITS_OF_ID}"
RELAY_TOPIC = "pr/home/9147953/sts"


def on_connect(client: mqtt.Client, userdata: Any, flags: dict, rc: int) -> None:
    if rc == 0:
        print("Connected to HiveMQ broker successfully!")
        client.subscribe(RELAY_TOPIC, qos=0)
        print(f"Subscribed to '{RELAY_TOPIC}'. Waiting for DHT sensor data...")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage) -> None:
    print(f"From TOPIC: {message.topic}")
    print(f"Message: {message.payload.decode()}")


if __name__ == "__main__":
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=CLIENT_ID, clean_session=False)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(broker_ip, int(broker_port))
    mqtt_client.loop_start()
    time.sleep(1)
    # according to the manual int the 4 dropbox this is the packet that we need to send to the IoT device
    on_payload = {"type": "set_state", "action": "set_value", "addr": 0, "cname": "ONOFF", "value": 1}
    mqtt_client.publish(RELAY_TOPIC, json.dumps(on_payload), qos=0)
    time.sleep(4)

    off_payload = {"type": "set_state", "action": "set_value", "addr": 0, "cname": "ONOFF", "value": 0}
    mqtt_client.publish(RELAY_TOPIC, json.dumps(off_payload), qos=0)
    time.sleep(2)

    mqtt_client.loop_stop()
    mqtt_client.disconnect()
