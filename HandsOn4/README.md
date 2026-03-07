# IoT Smart Home Emulation (MQTT)

This repository contains the client implementations and device emulators for a simulated Smart Home IoT environment. The project demonstrates the use of the MQTT protocol to collect sensor data, control hardware, and build event-driven integrations.

## Project Overview

The project is built using Python and the `paho-mqtt` library. It interacts with a public HiveMQ broker to communicate with various White-Cube device emulators.

The project is divided into three main tests (clients):

### 1. Test 1: Data Collection & Visualization (`test1_client.py`)
* **Goal:** Passively listen to a Temperature & Humidity sensor (DHT).
* **Operation:** Subscribes to the DHT emulator's status topic, collects 20 data samples, and parses the payload.
* **Bonus:** Utilizes `pandas` and `matplotlib` to automatically generate an Excel report and a visual graph (`output/DHT_Curves.png`) of the environmental changes over time.

### 2. Test 2: Remote Device Control (`test2_client.py`)
* **Goal:** Actively send state-changing commands to a Relay emulator.
* **Operation:** Uses `client.loop_start()` to run the network thread in the background. Publishes correctly formatted JSON commands (`{"type": "set_state", ...}`) to turn the Relay ON and OFF programmatically.

### 3. Test 3: Event-Driven Integration (`test3_client.py`)
* **Goal:** Create a smart hub that reacts to physical (emulated) events.
* **Operation:** Subscribes to a Button emulator. Upon detecting a button press event, the client processes the event, toggles its internal state, and publishes a JSON command to the Relay to turn it ON or OFF.

## File Structure
* `BUTTON.py`, `DHT.py`, `RELAY.py`: PyQT5-based IoT device emulators.
* `test*_client.py`: The MQTT client scripts implementing the logic.
* `mqtt_init.py`: Configuration file for broker IP and credentials.
* `output/`: Contains generated artifacts like the DHT data graphs.