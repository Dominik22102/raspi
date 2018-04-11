import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(22,gpio.OUT)

try:
	while(True):
		gpio.output(22,gpio.HIGH)
		time.sleep(1)
		gpio.output(22,gpio.LOW)
		time.sleep(1)
