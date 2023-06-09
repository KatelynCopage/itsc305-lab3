import RPi.GPIO as GPIO
from ADCDevice import *
import smbus
import time
import math

address = 0x48
bus=smbus.SMBus(1)
cmd=0x40

ledRedPin = 17
ledGreenPin = 27
ledBluePin = 22

def analogRead(chn):
	bus.write_byte(address,cmd+chn)
	value = bus.read_byte(address)
	return value

def analogWrite(value):
	bus.write_byte_data(address,cmd,value)

def setup():
	global p_Red,p_Green,p_Blue
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledRedPin,GPIO.OUT)
	GPIO.setup(ledGreenPin,GPIO.OUT)
	GPIO.setup(ledBluePin,GPIO.OUT)

	p_Red = GPIO.PWM(ledRedPin,1000)
	p_Red.start(0)
	p_Green = GPIO.PWM(ledGreenPin,1000)
	p_Green.start(0)
	p_Blue = GPIO.PWM(ledBluePin,1000)
	p_Blue.start(0)

def loop():
	while True:
		value_Red = analogRead(0)
		value_Green = analogRead(0)
		value_Blue = analogRead(0)
		p_Red.ChangeDutyCycle(value_Red*100/255)
		p_Green.ChangeDutyCycle(value_Green*100/255)
		p_Blue.ChangeDutyCycle(value_Blue*100/255)
		print ('ADC Value value_Red: %d ,\tvlue_Green: %d ,\tvalue_Blue:%d'%(value_Red,value_Green,value_Blue))
		time.sleep(0.01)

def destroy():
	bus.close()
	GPIO.cleanup()

if __name__ == '__main__': # Program entrance
        print ('Program is starting ... ')
        try:
                setup()
                loop()
        except KeyboardInterrupt: # Press ctrl-c to end the program.
                destroy()
