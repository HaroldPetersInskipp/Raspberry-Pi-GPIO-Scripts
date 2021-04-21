#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(20,19,21,active_high=True)

while True:
	#red
	led.color = (1,0,0)
	sleep(0.6)

	#rose
	led.color = (0.9,0,0.35)
	sleep(0.6)

	#purple
	led.color = (1,0,1)
	sleep(0.6)

	#violet
	led.color = (0.5,0,1)
	sleep(0.6)

	#blue
	led.color = (0,0,1)
	sleep(0.6)

	#azure
	led.color = (0,0.5,1)
	sleep(0.6)

	#cyan
	led.color = (0,1,1)
	sleep(0.6)

	#teal
	led.color = (0,1,0.5)
	sleep(0.6)

	#green
	led.color = (0,1,0)
	sleep(0.6)

	#lime
	led.color = (0.5,0.75,0)
	sleep(0.6)

	#yellow
	led.color = (0.85,0.9,0)
	sleep(0.6)

	#orange
	led.color = (0.8,0.2,0)
	sleep(0.6)
