import board
import digitalio
import time

# config digital inputs as outputs channels
relay1 = digitalio.DigitalInOut(board.GP0)
relay1.direction = digitalio.Direction.OUTPUT

# set your initial value state of the reles, my rele is set on True to be turn off
relay1.value = True

relay2 = digitalio.DigitalInOut(board.GP1)
relay2.direction = digitalio.Direction.OUTPUT
relay2.value = True

relay3 = digitalio.DigitalInOut(board.GP3)
relay3.direction = digitalio.Direction.OUTPUT
relay3.value = True

relay4 = digitalio.DigitalInOut(board.GP6)
relay4.direction = digitalio.Direction.OUTPUT
relay4.value = True

def channel_1 (value):
    state = value
    if value:
        relay1.value= False
    else:
        relay1.value= True


def channel_2 (value):
    state = value
    if value:
        relay2.value= False
    else:
        relay2.value= True


def channel_3 (value):

    state = value
    if value:
        relay3.value= False
    else:
        relay3.value= True


def channel_4 (value):

    state = value
    if value:
        relay4.value= False
    else:
        relay4.value= True




