# Smart Home GUI Dashboard (MQTT)

This repository contains a PyQt5-based Graphical User Interface (GUI) for monitoring and controlling a Smart Home environment via the MQTT protocol. This project was developed as part of Hands-On Assignment 6.

## 🚀 Project Overview

The application serves as a central hub (Dashboard) that allows users to connect to an MQTT broker, subscribe to sensor topics, and publish commands.

The core feature of this project is the **Automated Event Handler**:
The system continuously monitors incoming data from a simulated Temperature and Humidity (DHT) sensor. If the temperature exceeds a critical threshold (30.0°C), the system reacts automatically by:
1. **Triggering a UI Alarm:** Safely emitting a cross-thread signal to display a critical `QMessageBox` popup to the user.
2. **Controlling Hardware:** Automatically publishing a JSON-formatted `ON` command to a connected RELAY device to simulate activating a cooling system.

## 📁 File Structure
* `MonitorGui.py`: The main PyQt5 dashboard application containing the UI and the custom event-handling logic.
* `DHT.py`: Emulator for the temperature sensor.
* `RELAY.py`: Emulator for the relay module.
* `mqtt_init.py`: Configuration file containing the broker's IP and port.

## 🛠️ How to Run
1. Install required libraries: `pip install paho-mqtt PyQt5`
2. Start the device emulators: run `DHT.py` and `RELAY.py` in separate terminals and click "Connect" on both.
3. Start the dashboard: run `python MonitorGui.py`.
4. Click **Connect** in the main dashboard.
5. Click **Subscribe** to start receiving DHT sensor data.
6. **Trigger the Alarm:** In the DHT emulator, manually change the temperature to a value higher than `30.0`. The dashboard will immediately pop up an alarm and switch the Relay to ON.