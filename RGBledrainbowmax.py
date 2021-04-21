#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(20,19,21,active_high=True)

while True:
	#red
	led.color = (1,0,0)
	sleep(0.1)

	#.5
	led.color = (0.95,0,0.2)
	sleep(0.1)

	#rose
	led.color = (0.9,0,0.35)
	sleep(0.1)

	#.5
	led.color = (0.95,0,0.7)
	sleep(0.1)

	#purple
	led.color = (1,0,1)
	sleep(0.1)

	#.5
	led.color = (0.75,0,1)
	sleep(0.1)

	#violet
	led.color = (0.5,0,1)
	sleep(0.1)

	#.5
	led.color = (0.25,0,1)
	sleep(0.1)

	#blue
	led.color = (0,0,1)
	sleep(0.1)

	#.5
	led.color = (0,0.25,1)
	sleep(0.1)

	#azure
	led.color = (0,0.5,1)
	sleep(0.1)

	#.5
	led.color = (0,0.75,1)
	sleep(0.1)

	#cyan
	led.color = (0,1,1)
	sleep(0.1)

	#.5
	led.color = (0,1,0.75)
	sleep(0.1)

	#teal
	led.color = (0,1,0.5)
	sleep(0.1)

	#.5
	led.color = (0,1,0.28)
	sleep(0.1)

	#green
	led.color = (0,1,0)
	sleep(0.1)

	#.5
	led.color = (0.2,0.83,0)
	sleep(0.1)

	#lime
	led.color = (0.5,0.75,0)
	sleep(0.1)

	#.5
	led.color = (0.67,0.83,0)
	sleep(0.1)

	#yellow
	led.color = (0.85,0.9,0)
	sleep(0.1)

	#.5
	led.color = (0.82,0.55,0)
	sleep(0.1)

	#orange
	led.color = (0.8,0.2,0)
	sleep(0.1)

	#.5
	led.color = (0.9,0.15,0)
	sleep(0.1)
