import json
from typing import Any
import paho.mqtt.client as mqtt
from mqtt_init import *

LAST_FOUR_DIGITS_OF_ID = 6819
SIGNATURE_NAME = "AL"
CLIENT_ID = f"Iot_{SIGNATURE_NAME}_{LAST_FOUR_DIGITS_OF_ID}_Test3"

BUTTON_TOPIC = "pr/home/button_123_AL/sts"
RELAY_TOPIC = "pr/home/9147953/sts"

relay_state = 0


def on_connect(client: mqtt.Client, userdata: Any, flags: dict, rc: int) -> None:
    if rc == 0:
        print("Connected to HiveMQ broker successfully!")
        client.subscribe(BUTTON_TOPIC, qos=0)
        print(f"Subscribed to '{BUTTON_TOPIC}'. Waiting for BUTTON clicks...")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage) -> None:
    global relay_state

    payload_str = message.payload.decode()  # I will always get "value":1 from the BUTTON.py
    print(f"\n[EVENT] Message received from BUTTON: {payload_str}")

    relay_state = 1 if relay_state == 0 else 0

    command_payload = {
        "type": "set_state",
        "action": "set_value",
        "addr": 0,
        "cname": "ONOFF",
        "value": relay_state
    }

    print(f"[ACTION] Toggling RELAY to state: {'ON' if relay_state == 1 else 'OFF'}")
    client.publish(RELAY_TOPIC, json.dumps(command_payload), qos=0)


if __name__ == "__main__":
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=CLIENT_ID, clean_session=True)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(broker_ip, int(broker_port))
    mqtt_client.loop_forever()