#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(20,19,21,active_high=True)
led2 = RGBLED(13,18,17,active_high=True)

while True:
	#red
	led.color = (1,0,0)
	sleep(0.1)
	led.color = (0,0,0)
	sleep(0.1)

	#redR
	led2.color = (0,1,1)
	sleep(0.1)
	led2.color = (0,0,0)
	sleep(0.1)

	#purple
	led.color = (1,0,1)
	sleep(0.1)
	led.color = (0,0,0)
	sleep(0.1)

	#purpleR
	led2.color = (0,1,0)
	sleep(0.1)
	led2.color = (0,0,0)
	sleep(0.1)

	#blue
	led.color = (0,0,1)
	sleep(0.1)
	led.color = (0,0,0)
	sleep(0.1)

	#blueR
	led2.color = (1,1,0)
	sleep(0.1)
	led2.color = (0,0,0)
	sleep(0.1)

	#cyan
	led.color = (0,1,1)
	sleep(0.1)
	led.color = (0,0,0)
	sleep(0.1)

	#cyanR
	led2.color = (1,0,0)
	sleep(0.1)
	led2.color = (0,0,0)
	sleep(0.1)

	#green
	led.color = (0,1,0)
	sleep(0.1)
	led.color = (0,0,0)
	sleep(0.1)

	#greenR
	led2.color = (1,0,1)
	sleep(0.1)
	led2.color = (0,0,0)
	sleep(0.1)

	#yellow
	led.color = (1,1,0)
	sleep(0.1)
	led.color = (0,0,0)
	sleep(0.1)

	#yellowR
	led2.color = (0,0,1)
	sleep(0.1)
	led2.color = (0,0,0)
	sleep(0.1)
