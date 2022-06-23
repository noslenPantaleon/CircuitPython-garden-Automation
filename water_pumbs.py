import relays
import time
from countdown import countdown
import asyncio

# waterpump_sensor return this:  
# false= water level empty
# true = water level full
  

async def water_pumb_cycle (sensor_data):
    
    if sensor_data:
          
        relays.channel_2 (True)
        print ("channel_2 on")
        await asyncio.sleep(240)
        return
    else:
        relays.channel_2 (False)
        await asyncio.sleep(5)
        relays.channel_1 (True)
        print ("channel_1 on")
        await asyncio.sleep(240)
        relays.channel_1 (False)
        return
