import math
from gpiozero import PWMLED
from time import sleep
import smbus

red = PWMLED(17)
green = PWMLED(27)
blue = PWMLED(22)

#def turn_on():
#	for led in red
#		red.value == 0

#def hue(led):
#	hue = [0,0,0]
#	val = leds % 42.5
#	if leds <= 42.5:
#		hue[0] = 255
#		hue[1] = (val * 255) /42.5
#		hue[2] = 0
#	elif leds> 42.5 and leds <= 85:
#		hue[0] = 255 - (120)

def cycle():
	red.value = sin(120)
	blue.value = sin(120 +120)
	green.value = sin(120+240)

i2c_bus = smbus.
