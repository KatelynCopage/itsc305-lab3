# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADS7830
# This code is designed to work with the ADS7830_I2CADC_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=ADS7830_I2CADC#tabs-0-product_tabset-2

from gpiozero import PWMLED
import smbus
from time import sleep
import math
# Get I2C bus
bus = smbus.SMBus(1)

red = PWMLED(17)
green = PWMLED(27)
blue = PWMLED(22)

while True:
	# ADS7830 address, 0x4b
	# Send command byte
	#		0x8C	Single ended inputs, Channel-0
	bus.write_byte(0x4b, 0x8C)

	sleep(0.1)

	# ADS7830 address, 0x48(72)
	# Read data back, 1 byte
	data = bus.read_byte(0x4b)

	# Output data to screen
	print ("Digital value of analog input :", data)

	degrees = (data / 255) * 359
	print(degrees)

	red_pwm = (math.sin(degrees) / 2) + 0.5
	blue_pwm = (math.sin(degrees + 120) / 2) + 0.5
	green_pwm = (math.sin(degrees + 240) / 2) + 0.5
	print(red_pwm, blue_pwm, green_pwm)

	red.value = red_pwm
	sleep(0.9)
	green.value = green_pwm
	sleep(0.9)
	blue.value = blue_pwm

#write_byte(address, command)

#command - 1 0 0 0 1 1 0 0 -> 0x8C
