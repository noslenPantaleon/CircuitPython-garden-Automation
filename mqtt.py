import board
import busio
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import json
from funtions import data, waterpumbs_cycle_on, waterpumbs_cycle_off
import relays

mqtt_topic = "gardenData"
mqtt_recieved = "brokerData"

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account

aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

# If you are using a board with pre-defined ESP32 Pins:
# esp32_cs = DigitalInOut(board.ESP_CS)
# esp32_ready = DigitalInOut(board.ESP_BUSY)
# esp32_reset = DigitalInOut(board.ESP_RESET)

# If you have an externally connected ESP32:
esp32_cs = DigitalInOut(board.GP7)
esp32_ready = DigitalInOut(board.GP10)
esp32_reset = DigitalInOut(board.GP11)
spi = busio.SPI(board.GP18, board.GP19, board.GP16)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("could not connect to AP, retrying: ", e)
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)

# Define callback methods which are called when events occur
def connect(mqtt_client, userdata, flags, rc):
    # This function will be called when the mqtt_client is connected
    # successfully to the broker.
    print("Connected to MQTT Broker!")
    print("Flags: {0}\n RC: {1}".format(flags, rc))


def disconnect(mqtt_client, userdata, rc):
    # This method is called when the mqtt_client disconnects
    # from the broker.
    print("Disconnected from MQTT Broker!")


def subscribe(mqtt_client, userdata, topic, granted_qos):
    # This method is called when the mqtt_client subscribes to a new feed.
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))


def unsubscribe(mqtt_client, userdata, topic, pid):
    # This method is called when the mqtt_client unsubscribes from a feed.
    print("Unsubscribed from {0} with PID {1}".format(topic, pid))


def publish(mqtt_client, userdata, topic, pid):


    # This method is called when the mqtt_client publishes data to a feed.
    print("Published to {0} with PID {1}".format(topic, pid))

def message(client, topic, message):

    sensor_data = data

    print ("New message on topic {0}: {1}".format(topic, message))
    if message == "send_report":
        jsonData = json.dumps(sensor_data)
        mqtt_client.publish(mqtt_topic, jsonData)

    elif message == "relay1_on":
        relays.channel_1 (True)

    elif message == "relay1_off":
        relays.channel_1 (False)

    elif message == "relay2_on":
        relays.channel_2 (True)

    elif message == "relay2_off":
        relays.channel_2 (False)

    elif message == "relay3_on":
        relays.channel_3 (True)

    elif message == "relay3_off":
        relays.channel_3 (False)

    elif message == "relay4_on":
        relays.channel_4 (True)

    elif message == "relay4_off":
        relays.channel_4 (False)
        
    elif message == "waterpumbs_on":
        waterpumbs_cycle_on()
        
    elif message == "waterpumbs_off":
        waterpumbs_cycle_off()

socket.set_interface(esp)
MQTT.set_socket(socket, esp)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=secrets["broker"],
    port=secrets["port"],
    username=secrets["username"],
    password=secrets["password"],
)


# Connect callback handlers to mqtt_client
mqtt_client.on_connect = connect
mqtt_client.on_disconnect = disconnect
mqtt_client.on_subscribe = subscribe
mqtt_client.on_unsubscribe = unsubscribe
mqtt_client.on_publish = publish
mqtt_client.on_message = message

print("Attempting to connect to %s" % mqtt_client.broker)
mqtt_client.connect()

print("Subscribing to %s" % mqtt_topic)
mqtt_client.subscribe(mqtt_topic)
mqtt_client.subscribe(mqtt_recieved)
broker_message= message(mqtt_client, mqtt_recieved, message)


# print("Unsubscribing from %s" % mqtt_topic)
# mqtt_client.unsubscribe(mqtt_topic)
#
# print("Disconnecting from %s" % mqtt_client.broker)
# mqtt_client.disconnect()
