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
	sleep(0.02)
	yellow.off()
	sleep(0.02)
	blue.on()
	sleep(0.02)
	white.off()
	sleep(0.02)
	green.on()
	sleep(0.02)
	blue.off()
	sleep(0.02)
	yellow.on()
	sleep(0.02)
	yellow.off()
	sleep(0.02)
	green.off()
	sleep(0.02)
	blue.on()
	sleep(0.02)
	white.on()
	sleep(0.02)
	blue.off()
	sleep(0.02)
	white.off()
	sleep(0.02)
	red.on()
	sleep(0.02)
	yellow.on()
	sleep(0.02)
	blue.on()
	sleep(0.02)
	yellow.off()
	sleep(0.02)
	red.off()
	sleep(0.02)
	red.on()
	sleep(0.02)
	blue.off()
	sleep(0.02)
	yellow.on()
	sleep(0.02)
	red.off()
	sleep(0.02)
	green.on()
	sleep(0.02)
	green.off()
	sleep(0.02)
