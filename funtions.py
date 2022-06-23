import oled_sh1106
from oled_sh1106 import oled, bmp_image
import adafruit_displayio_sh1106
from sensors import readHTU21D_sensor, watertemp_sensor, water_level_sensor
from adafruit_htu21d import HTU21D
from adafruit_display_text import label
import displayio
import terminalio
import board
import digitalio
import busio
import time
import adafruit_ds3231
import relays

# Create library object using our Bus I2C port
i2c = busio.I2C(board.GP5, board.GP4)
i2c2 = busio.I2C(board.GP27, board.GP14)

#calling HTU21D funtion with i2c port
sensor_HTU21D_1 = readHTU21D_sensor(i2c)

rtc = adafruit_ds3231.DS3231(i2c)

#calling HTU21D funtion with i2c port
sensor_HTU21D_2 = readHTU21D_sensor(i2c2)

#calling watertemp sensor funtion
sensor_DS18B20 = watertemp_sensor(board.GP13)

#calling waterlevel sensor funtion
water_level_pin = digitalio.DigitalInOut(board.GP17)
water_level_pin.direction = digitalio.Direction.INPUT

#display oled config
WIDTH = 128
HEIGHT = 64
BORDER = 1
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c2, device_address=0x3c)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

# create a dictionaty to estructure the sensor data
data = {}

# initialized sensor variables
temp_1 = 0
temp_2 = 0
hum_1 = 0
hum_2 = 0
water_temp = 0
water_level = 0
pumps = 0

icon_temperature = "icons/temperature.bmp"
icon_humidity= "icons/humidity.bmp"
icon_water_level= "icons/water.bmp"
icon_sunnny = "icons/sunny.bmp"
icon_water_temp = "icons/water_temp.bmp"

# pylint: disable-msg=using-constant-test
if False:  # change to True if you want to set the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2022, 05, 06, 21, 35, 00, 0, -1, -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
#     print("Setting time to:", t)  # uncomment for debugging
    rtc.datetime = t

# pylint: enable-msg=using-constant-test

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def data_sensors():

    global data
    global temp_1
    global temp_2
    global hum_2
    global water_temp
    global water_level
    global pumps

    # saving data into new variables
    temp_1 = sensor_HTU21D_1.temperature
    temp_2 = sensor_HTU21D_2.temperature
    hum_1 = sensor_HTU21D_1.relative_humidity
    hum_2 = sensor_HTU21D_2.relative_humidity
    water_temp = sensor_DS18B20
    water_level = water_level_sensor (water_level_pin)


    # asssign keys and value of the dictionary with the sensor data
    data["temp1"] = temp_1
    data["hum1"] = hum_1
    data["temp2"] = temp_2
    data["hum2"] = hum_2
    data["watertemp"] = water_temp
    data["waterlevel"] = water_level



def display_oled():

    t = rtc.datetime
    hour=t.tm_hour
    minutes=t.tm_min
    seconds= t.tm_sec
    display_time= (str(hour)+ ":" + str(minutes))

    screen1 = oled ( "\nTemp1: \n%0.1f C" % temp_1, icon_temperature, display_time)
    screen2 = oled ( "\nTemp2: \n%0.1f C" % temp_2, icon_temperature, display_time)
    screen3 = oled ( "\nHum1: \n%0.1f " % hum_1, icon_humidity, display_time)
    screen4 = oled ( "\nHum2: \n%0.1f " % hum_2, icon_humidity, display_time)
    screen5 = oled ("\nh20temp: \n%0.1f C" % water_temp, icon_water_temp, display_time)
    screen6 = oled ("\nh2oLvl: \n%0.1f " % water_level, icon_water_level, display_time)



    # display oled screens
    display.show(screen1)
    time.sleep(2)
    display.show(screen2)
    time.sleep(2)
    display.show(screen3)
    time.sleep(2)
    display.show(screen4)
    time.sleep(2)
    display.show(screen5)
    time.sleep(2)
    display.show(screen6)
    time.sleep(2)



def  waterpumbs_cycle_off():
    relays.channel_1 (False)
    relays.channel_2 (False)
    print ("cycle off")

def  waterpumbs_cycle_on():
    t= rtc.datetime
    hour=t.tm_hour
    minutes=t.tm_min
    seconds=t.tm_sec
    print ("cycle on")

#alarm 6 am
    if hour == 6  and minutes== 00:
         relays.channel_1 (True)
    elif hour == 6  and minutes== 01:
         relays.channel_1 (False)

    if hour == 6  and minutes== 10:
         relays.channel_2 (True)
    elif hour == 6 and minutes== 13:
         relays.channel_2 (False)
 #alarm 8 am
    if hour == 8  and minutes== 00:
     relays.channel_1 (True)
    elif hour == 8  and minutes== 01:
         relays.channel_1 (False)

    if hour == 8  and minutes== 10:
         relays.channel_2 (True)
    elif hour == 8 and minutes== 13:
         relays.channel_2 (False)
#alarm 10 am
    if hour ==10  and minutes== 00:
         relays.channel_1 (True)
    elif hour == 10   and minutes== 01:
         relays.channel_1 (False)

    if hour == 10   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 10  and minutes== 13:
         relays.channel_2 (False)

#alarm 12 am
    if hour ==12  and minutes== 00:
         relays.channel_1 (True)
    elif hour == 12   and minutes== 01:
         relays.channel_1 (False)

    if hour == 12   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 12  and minutes== 13:
         relays.channel_2 (False)

#alarm 14
    if hour ==14  and minutes== 00:
         relays.channel_1 (True)
    elif hour == 14   and minutes== 01:
         relays.channel_1 (False)

    if hour == 14   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 14  and minutes== 13:
         relays.channel_2 (False)

#alarm 16
    if hour == 16   and minutes== 00:
         relays.channel_1 (True)
    elif hour == 16  and minutes== 01:
         relays.channel_1 (False)

    if hour == 16   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 16  and minutes== 13:
         relays.channel_2(False)

 #alarm 18
    if hour == 18   and minutes== 00:
         relays.channel_1 (True)
    elif hour == 18  and minutes== 01:
         relays.channel_1 (False)

    if hour == 18  and minutes== 10:
         relays.channel_2 (True)
    elif hour ==18  and minutes== 13:
         relays.channel_2 (False)
 #alarm 20
    if hour == 20   and minutes== 00:
         relays.channel_1 (True)
    elif hour == 20  and minutes== 01:
         relays.channel_1 (False)

    if hour == 20   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 20  and minutes== 13:
         relays.channel_2 (False)

 #alarm 22
    if hour == 22   and minutes== 00:
         relays.channel_1 (True)
    elif hour == 22  and minutes== 01:
         relays.channel_1 (False)

    if hour == 22   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 22  and minutes== 13:
         relays.channel_2 (False)

 #alarm 24
    if hour == 24   and minutes== 00:
         relays.channel_1 (True)
    elif hour == 24 and minutes== 01:
         relays.channel_1 (False)

    if hour == 24  and minutes== 10:
         relays.channel_2 (True)
    elif hour == 24  and minutes== 13:
         relays.channel_2 (False)
 #alarm 2 am
    if hour == 2   and minutes== 00:
         relays.channel_1 (True)
    elif hour == 2  and minutes== 01:
         relays.channel_1 (False)

    if hour == 2   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 2  and minutes== 13:
         relays.channel_2 (False)
#alarm 4 am
    if hour == 4   and minutes== 00:
         relays.channel_1 (True)
    elif hour == 4  and minutes== 01:
         relays.channel_1 (False)

    if hour == 4   and minutes== 10:
         relays.channel_2 (True)
    elif hour == 4  and minutes== 13:
         relays.channel_2 (False)
