#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(20,19,21,active_high=True)

while True:
	#red
	led.color = (1,0,0)
	sleep(0.05)

	#.5
	led.color = (1,0,0.25)
	sleep(0.05)

	#rose
	led.color = (0.95,0,0.4)
	sleep(0.05)

	#.5
	led.color = (0.9,0,0.7)
	sleep(0.05)

	#purple
	led.color = (0.9,0,1)
	sleep(0.05)

	#.5
	led.color = (0.75,0,1)
	sleep(0.05)

	#violet
	led.color = (0.5,0,1)
	sleep(0.05)

	#.5
	led.color = (0.3,0,1)
	sleep(0.05)

	#blue
	led.color = (0,0,1)
	sleep(0.05)

	#.5
	led.color = (0,0.3,1)
	sleep(0.05)

	#azure
	led.color = (0,0.5,1)
	sleep(0.05)

	#.5
	led.color = (0,0.75,1)
	sleep(0.05)

	#cyan
	led.color = (0,1,1)
	sleep(0.05)

	#.5
	led.color = (0,1,0.75)
	sleep(0.05)

	#teal
	led.color = (0,1,0.5)
	sleep(0.05)

	#.5
	led.color = (0,1,0.3)
	sleep(0.05)

	#green
	led.color = (0,1,0)
	sleep(0.05)

	#.5
	led.color = (0.25,0.83,0)
	sleep(0.05)

	#lime
	led.color = (0.5,0.75,0)
	sleep(0.05)

	#.5
	led.color = (0.7,0.83,0)
	sleep(0.05)

	#yellow
	led.color = (1,1,0)
	sleep(0.05)

	#.5
	led.color = (0.78,0.5,0)
	sleep(0.05)

	#orange
	led.color = (0.7,0.25,0)
	sleep(0.05)

	#.5
	led.color = (0.9,0.2,0)
	sleep(0.05)
