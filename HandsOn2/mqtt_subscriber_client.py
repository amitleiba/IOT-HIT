import time

import paho.mqtt.client as mqtt  # import the client1

# broker list
brokers = ["iot.eclipse.org", "broker.hivemq.com", \
           "test.mosquitto.org"]

broker = brokers[1]


def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected result code " + str(rc))


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("Now message received: ", m_decode)
    print("It was topic: ", topic)
    if "send message" in m_decode:
        client.publish(pub_topic, 'returned message')


client = mqtt.Client("IOT_dvfxxiaeurfrfrsdsfiu021_AL6819", clean_session=True)  # create new client instance

client.on_connect = on_connect  # bind call back function
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_message = on_message

print("Connecting to broker ", broker)
port = 1883
client.connect(broker, port)  # connect to broker

sub_topic = 'house/sensor/AL19'
pub_topic = 'house/sensor/AL/pub'

client.loop_start()  # Start loop
client.subscribe(sub_topic)
time.sleep(10)
client.loop_stop()  # Stop loop
client.disconnect()
