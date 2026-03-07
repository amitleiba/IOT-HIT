from typing import Any

import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
import pandas as pd

from mqtt_init import *

LAST_FOUR_DIGITS_OF_ID = 6819
SIGNATURE_NAME = "AL"
CLIENT_ID = f"Iot_{SIGNATURE_NAME}_{LAST_FOUR_DIGITS_OF_ID}"
DHT_TOPIC = 'pr/home/5976397/sts'
MAX_MESSAGES = 20

data_records = []


def on_connect(client: mqtt.Client, userdata: Any, flags: dict, rc: int) -> None:
    if rc == 0:
        print("Connected to HiveMQ broker successfully!")
        client.subscribe(DHT_TOPIC, qos=0)
        print(f"Subscribed to '{DHT_TOPIC}'. Waiting for DHT sensor data...")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage) -> None:
    global data_records

    payload_str = message.payload.decode()
    parts = payload_str.split()

    try:
        if len(parts) >= 4 and parts[0] == "Temperature:" and parts[2] == "Humidity:":
            temp = float(parts[1])
            hum = float(parts[3])

            data_records.append({"Temperature": temp, "Humidity": hum})

            current_count = len(data_records)
            print(f"[Sample {current_count}/{MAX_MESSAGES}] Temp: {temp}°C | Humidity: {hum}%")
            if current_count >= MAX_MESSAGES:
                print("\nCollected 20 samples! Disconnecting from broker...")
                client.disconnect()

    except ValueError:
        print("Received unparsable data:", payload_str)


def data_to_excel():
    print("Generating Excel file and graphs...")
    df = pd.DataFrame(data_records)

    excel_filename = "./output/DHT_Data.xlsx"
    df.to_excel(excel_filename, index=False)
    print(f"Data successfully saved to {excel_filename}")

    plt.figure(figsize=(10, 5))
    plt.plot(df.index + 1, df["Temperature"], label="Temperature (°C)", color="red", marker="o")
    plt.plot(df.index + 1, df["Humidity"], label="Humidity (%)", color="blue", marker="s")

    plt.title("DHT Sensor Data Over Time")
    plt.xlabel("Sample Number")
    plt.ylabel("Sensor Values")
    plt.grid(True)
    plt.legend()

    plt.savefig("./output/DHT_Curves.png")
    print("Graph saved as DHT_Curves.png")
    plt.show()


if __name__ == "__main__":
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=CLIENT_ID, clean_session=False)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(broker_ip, int(broker_port))
    mqtt_client.loop_forever()
    data_to_excel()
