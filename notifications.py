from funtions import data
from mqtt import mqtt_client, publish
mqtt_topic = "gardenData"
mqtt_recieved = "brokerData"

def check_waterlevel():

    watertank =  data['waterlevel']
    if watertank:
        pass

    else:
        mqtt_client.publish(mqtt_topic, f"  low waterlevel = {watertank}")

