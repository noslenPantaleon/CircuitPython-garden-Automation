from funtions import data_sensors, display_oled
from mqtt import mqtt_client, publish
from notifications import check_waterlevel
import time

while True:

    if not mqtt_client:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        mqtt_client.reconnect()


    else:
        data_sensors()
        display_oled()
        check_waterlevel()
        mqtt_client.loop()
    time.sleep(1)


