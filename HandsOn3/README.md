# IoT Smart City - MQTT Client (Hands-On 3)

This repository contains the Python implementation for Hands-On Assignment 3 of the "Software Development for IoT Systems in a Smart City Environment" course. 

## Overview
[cite_start]The project demonstrates the core concepts of the MQTT protocol using the `paho-mqtt` library[cite: 129]. [cite_start]It includes a test suite that explores the behavior of an MQTT broker under different connection states, QoS levels, and message configurations[cite: 78, 122].

## Features Tested
* [cite_start]**Quality of Service (QoS):** Testing levels 0 and 1 for both publishing and subscribing[cite: 95, 107].
* [cite_start]**Clean Session:** Analyzing the broker's message queueing behavior with `clean_session` set to `True` and `False`[cite: 94, 99].
* [cite_start]**Retained Messages:** Implementing sticky messages that remain on the broker for new subscribers[cite: 79].
* [cite_start]**Last Will and Testament (LWT):** Setting up automatic offline notifications for unexpected client disconnections[cite: 80].

## Prerequisites
* Python 3.x
* [cite_start]`paho-mqtt` library (`pip install paho-mqtt`) [cite: 31, 32]

## Usage
[cite_start]The main script contains 5 distinct tests based on the assignment requirements[cite: 78]. To test a specific scenario:
1. Uncomment the desired test in the `__main__` block.
2. Run the script: `python mqtt_client.py`
3. [cite_start]Use the [HiveMQ Web Client](http://www.hivemq.com/demos/websocket-client/) [cite: 135] to monitor the `iot/home_AL/...` topics and interact with the Python client.

## Author
**Amit Leiba**