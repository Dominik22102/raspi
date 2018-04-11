import RPi.GPIO as gpio
for time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(22,gpio.OUT)
gpio.setup(6, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.output(22, False

try:
	while True:
		gpio.output(22, gpio.input(6))
		sleep(.1)

finally:
	gpio.output(22, False)
	gpio.cleanup()