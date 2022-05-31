from pulsesensor import Pulsesensor

import time

import Adafruit_SSD1306 

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
servoleft = Servo(18, pin_factory=factory)
servoright = Servo(21, pin_factory=factory)

p = Pulsesensor()
p.startAsyncBPM()

RST = 24

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

x = padding

font = ImageFont.load_default()

draw.rectangle((0,0,width,height), outline=0, fill=0)
disp.image(image)
disp.display()

# perc = 0

# draw.rectangle((x, top, x+shape_width, (height-2)*perc), outline=255, fill=0)

disp.image(image)
disp.display()

while True:
	
	servoleft.mid()
	servoright.mid()
	time.sleep(3)
#	draw.rectangle((0,0,width,height), outline=0, fill=0)
#	time.sleep(1) 
#	draw.text((x, top),	'Please place the pad of your finger on the pulse sensor.', font=font, fill=255)
#	time.sleep(3)
#	draw.rectangle((0,0,width,height), outline=0, fill=0)

	bpm = p.BPM
	print(bpm)
	
	if bpm > 0: 
		draw.text((x, top),	'Hello. I am Baymax,', font=font, fill=255)
		draw.text((x, top+10),	'your personal', font=font, fill=255)
		draw.text((x, top+20),	'healthcare companion.', font=font, fill=255)
		draw.text((x, top+30),	'Your heartrate is', font=font, fill=255)
		draw.text((x, top+40),	str(int(bpm)), font=font, fill=255)
		disp.image(image)
		disp.display()
		time.sleep(2)
		draw.rectangle((0,0,width,height), outline=0, fill=0)
# print(bpm)
	else:
		draw.text((x, top),	'No heartbeat found', font=font, fill=255)
		disp.image(image)
		disp.display()
		time.sleep(2)
		draw.rectangle((0,0,width,height), outline=0, fill=0)
		time.sleep(2)


#			print("No heartbeat found")
		
# except:
#	draw.rectangle((0,0,width,height), outline=0, fill=0)
#	draw.text((x, top),	"Done", font=font, fill=255)
# 	p.stopAsyncBPM()
