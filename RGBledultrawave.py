#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

red = LED(20,active_high=True)
yellow = LED(18,active_high=True)
green = LED(19,active_high=True)
blue = LED(21,active_high=True)
white = LED(26,active_high=True)

while True:
	white.on()
	sleep(0.05)
	#white.off()
	#sleep(1)
	blue.on()
	sleep(0.05)
	#blue.off()
	#sleep(1)
	green.on()
	sleep(0.05)
	#green.off()
	#sleep(1)
	yellow.on()
	sleep(0.05)
	#yellow.off()
	#sleep(1)
	red.on()
	sleep(0.05)
	red.off()
	sleep(0.05)
	yellow.off()
	sleep(0.05)
	green.off()
	sleep(0.05)
	blue.off()
	sleep(0.05)
	white.off()
	sleep(0.05)