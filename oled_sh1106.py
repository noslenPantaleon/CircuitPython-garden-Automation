import busio
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import adafruit_displayio_sh1106
import adafruit_imageload
import time

displayio.release_displays()

WIDTH = 128
HEIGHT = 64
BORDER = 2

def oled (data, image_path, display_time):
    # Make the display context
    font = bitmap_font.load_font("/Adobe-Helvetica-Bold-R-Normal--12.bdf")
    font2= terminalio.FONT
    splash = displayio.Group(scale=1)
#     display.show(splash)

    color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

        # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 2)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
    )
    splash.append(inner_sprite)



    # Draw a label
    text = data
    text_area = label.Label(
         font, text=text, color=0xFFFFFF, x=45, y= 0, scale=1
    )
    splash.append(text_area)
    
    
    # Draw a label
    text2 = display_time
    text2_area = label.Label(
         font2, text=text2, color=0xFFFFFF, x=90, y= 8, scale=1
    )
    splash.append(text2_area)
    



    # load image

    icon= image_path
    sprite_sheet, palette = adafruit_imageload.load(icon,
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

    palette.make_transparent(0)

    # Create the sprite TileGrid
    sprite = displayio.TileGrid(
        sprite_sheet,
        pixel_shader=palette,
        width=1,
        height=1,
        tile_width=35,
        tile_height=35,
        default_tile=0,
        x=5,
        y=15,

    )


    # Add the TileGrid to the Group
    splash.append(sprite)


    return splash

def bmp_image ():

    # Setup the file as the bitmap data source
   # bitmap = displayio.OnDiskBitmap("/brote.bmp")

    sprite_sheet, palette = adafruit_imageload.load("/brote.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)




    # make the color at 0 index transparent.
    palette.make_transparent(0)

    # Create the sprite TileGrid
    sprite = displayio.TileGrid(
        sprite_sheet,
        pixel_shader=palette,
        width=1,
        height=1,
        tile_width=35,
        tile_height=35,
        default_tile=0,
    )



    # Create a TileGrid to hold the bitmap
    #tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

    # Create a Group to hold the TileGrid
    group = displayio.Group()

    # Add the TileGrid to the Group
    group.append(sprite)

    # Add the Group to the Display
    return group



