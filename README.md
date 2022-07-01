# CircuitPython-garden-Automation

❤️🍀🌱 "Working Progress" 🍀🌱❤️

### Description:

Portable Device to Make your automations and data logger for your crops, I am developinmg this open source system using Circuit Python, and Rasberrry pi pico with an esp32 wifi shield to send the data over mqtt to and rasberry pi broker or any broker you use.

### Harware:

Raspberry Pi Pico.
Pimoroni Pico Wireless shield.  
1 Lm2596 Step-down Dc-dc 1,23-35v 3a Display.
1 Sparkfun Logic Level Converter - Bi-directional.
1 portable power suply 12 volt, 2 amperes.
4 female Input 220v/110v conectors + cables.
Riel dims for the 220volt female imputs conectors.
terminals block to separete 3v/5v/12v.
1 4 channel 5volts relay (to use with any actuator, like waterpumps, lights, coolers, etc).
Display Oled 1.3 Azul 128x64 I2c Arduino Ssh1106.
reloj RTC ds3231.
1 water temperature level Ds18b20.
1 Water Level Sensor 45mm N/c N/a Floating Stainless Steel.
2 sensors temperature and humidity SHT21/HTU21 I2C.
Automation:
the automations can be set on the circuit-python code, but I prefer to use this box as only a harwared device to get data and control waterpumps, and lights over mqtt messages to activate funtions.

### Mqtt broker:

I use mosquitto broker running in my localhost on the raspberry pi 3, recieving and sending messages to the Rasberry Pi Pico.

### data logger:

I and devoloping an Api to save all the data into mongodb database, the main idea of the Api is to be scaleable and control too many crops with a simple working with a CRUD system (create/read/updated/save/delete) to manipulate all your differents crops. Also the Pimoroni shield has an sd card to save the data, this code is not already developed for now.

This api can be control with an frontend application using react-nextjs or any other technologic or framework.

You can download and check the working progress of the Python API here: https://github.com/noslenPantaleon/microsation_database_python_Api

### Industrial Design and pcb:

For now, I am testing this setup, this is a "preprototype". if this setup works good I will need some help to make an nice industrial design, and print the pcb board.

### Links:

https://circuitpython.org/
(https://www.raspberrypi.com/products/raspberry-pi-pico/)
(https://shop.pimoroni.com/products/pico-wireless-pack?variant=32369508581459)
https://fastapi.tiangolo.com/re
https://mosquitto.org/blog/2013/01/mosquitto-debian-repository/
