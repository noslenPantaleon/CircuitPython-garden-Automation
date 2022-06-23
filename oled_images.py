import board
import displayio
import busio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import adafruit_displayio_sh1106
import time

displayio.release_displays()

WIDTH = 128
HEIGHT = 64
BORDER = 1



#display oled config
i2c = busio.I2C(board.GP27, board.GP14)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)



# Current method valid for CircuitPython 6 & 7

# Open the file
with open("/brote.bmp", "rb") as bitmap_file:
    
    # Setup the file as the bitmap data source
    bitmap = displayio.OnDiskBitmap("/brote.bmp")
    
    
    

    # Create a TileGrid to hold the bitmap
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    

    # Create a Group to hold the TileGrid
    group = displayio.Group()

    # Add the TileGrid to the Group
    group.append(tile_grid)

    # Add the Group to the Display
    display.show(group)

    # Loop forever so you can enjoy your image
while True:
    pass