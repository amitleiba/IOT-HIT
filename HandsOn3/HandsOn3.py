import time
from typing import Any

import paho.mqtt.client as mqtt

LAST_FOUR_DIGITS_OF_ID = 6819
SIGNATURE_NAME = "AL"
TOPIC = f"iot/home_{SIGNATURE_NAME}/sensor_{LAST_FOUR_DIGITS_OF_ID}"
TEST_TOPIC = "testtopic/Hi"
CLIENT_ID = f"Iot_{SIGNATURE_NAME}_{LAST_FOUR_DIGITS_OF_ID}"
BROKER_HOSTNAME = "broker.hivemq.com"
RETAIN_MESSAGE = f"Hello My Name Is Amit Leiba. Client ID: {CLIENT_ID}"
LAST_WILL_MESSAGE = f"Goodbye everyone. Client ID: {CLIENT_ID}"


class IoTClient:
    def __init__(self, *, clean_session: bool, qos_publish: int, qos_subscribe: int) -> None:
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=CLIENT_ID, clean_session=clean_session)
        self.qos_publish = qos_publish
        self.qos_subscribe = qos_subscribe
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client: mqtt.Client, userdata: Any, flags: dict, rc: int) -> None:
        if rc == 0:
            print("Successfully connected")
            self.client.subscribe(TOPIC, qos=self.qos_subscribe)
        else:
            print(f"Connection failed with code: {rc}")

    def on_message(self, client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage) -> None:
        print(f"From TOPIC: {message.topic}")
        print(f"Message: {message.payload.decode()}")
        self.client.publish(TEST_TOPIC, RETAIN_MESSAGE.encode(), qos=self.qos_publish, retain=True)

    def run(self) -> None:
        self.client.will_set(TOPIC, LAST_WILL_MESSAGE.encode(), qos=self.qos_publish)
        self.client.connect(host=BROKER_HOSTNAME, port=1883, keepalive=90)
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()


if __name__ == "__main__":
    x = "=" * 5
    print(f"{x} Hands On 3 Task {x}")
    print("TEST 1:")
    test1 = IoTClient(clean_session=True, qos_publish=0, qos_subscribe=0)
    test1.run()
    time.sleep(15)
    test1.stop()
    print(x)

    print("TEST 2:")
    test2 = IoTClient(clean_session=False, qos_publish=0, qos_subscribe=0)
    test2.run()
    time.sleep(15)
    test2.stop()
    print(x)

    print("TEST 3:")
    test3 = IoTClient(clean_session=True, qos_publish=1, qos_subscribe=1)
    test3.run()
    time.sleep(15)
    test3.stop()
    print(x)

    print("TEST 4:")
    test4 = IoTClient(clean_session=False, qos_publish=1, qos_subscribe=1)
    test4.run()
    time.sleep(15)
    test4.stop()
    print(x)

    print("TEST 5:")
    test5 = IoTClient(clean_session=False, qos_publish=0, qos_subscribe=1)
    test5.run()
    time.sleep(15)
    test5.stop()
    print(x)
