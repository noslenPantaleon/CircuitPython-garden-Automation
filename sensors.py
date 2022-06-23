from adafruit_htu21d import HTU21D
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
import board
import digitalio

def readHTU21D_sensor (i2c):
    sensor = HTU21D(i2c)
    return sensor

def watertemp_sensor (pin):
    ow_bus = OneWireBus(pin)
    ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
    return ds18.temperature

def water_level_sensor (sensor_data):
    water_level = sensor_data.value
    return water_level


