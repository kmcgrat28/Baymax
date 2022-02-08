import time

import Adafruit_SSD1306
import Adafruit_GPIO.SPI as SPI

# from PIL 
import Image
# from PIL 
import ImageDraw
# from PIL 
import ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding

draw.text((x, top+10),   'Hello, world!',   font=font, fill=255)
