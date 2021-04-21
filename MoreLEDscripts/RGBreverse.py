#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(20,19,21,active_high=True)
led2 = RGBLED(13,18,17,active_high=True)

while True:
	#red
	led.color = (1,0,0)
	sleep(0.12)

	#.5
	led.color = (1,0,0.25)
	sleep(0.05)

	#red
	led2.color = (0,1,1)
	sleep(0.12)

	#.5
	led2.color = (0,1,0.75)
	sleep(0.05)

	#rose
	led.color = (0.95,0,0.4)
	sleep(0.06)

	#.5
	led.color = (0.9,0,0.75)
	sleep(0.05)

	#rose
	led2.color = (0.05,1,0.6)
	sleep(0.06)

	#.5
	led2.color = (0.1,1,0.25)
	sleep(0.05)

	#purple
	led.color = (0.9,0,1)
	sleep(0.07)

	#.5
	led.color = (0.77,0,1)
	sleep(0.05)

	#purple
	led2.color = (0.1,1,0)
	sleep(0.07)

	#.5
	led2.color = (0.23,1,0)
	sleep(0.05)

	#violet
	led.color = (0.6,0,1)
	sleep(0.06)

	#.5
	led.color = (0.3,0,1)
	sleep(0.05)

	#violet
	led2.color = (0.4,1,0)
	sleep(0.06)

	#.5
	led2.color = (0.7,1,0)
	sleep(0.05)

	#blue
	led.color = (0,0,1)
	sleep(0.12)

	#.5
	led.color = (0,0.2,1)
	sleep(0.05)

	#blue
	led2.color = (1,1,0)
	sleep(0.12)

	#.5
	led2.color = (1,0.8,0)
	sleep(0.05)

	#azure
	led.color = (0,0.35,1)
	sleep(0.06)

	#.5
	led.color = (0,0.6,1)
	sleep(0.05)

	#azure
	led2.color = (1,0.65,0)
	sleep(0.06)

	#.5
	led2.color = (1,0.4,0)
	sleep(0.05)

	#cyan
	led.color = (0,0.8,1)
	sleep(0.07)

	#.5
	led.color = (0,0.9,0.8)
	sleep(0.05)

	#cyan
	led2.color = (1,0.2,0)
	sleep(0.07)

	#.5
	led2.color = (1,0.1,0.2)
	sleep(0.05)

	#teal
	led.color = (0,0.9,0.65)
	sleep(0.06)

	#.5
	led.color = (0,1,0.45)
	sleep(0.05)

	#teal
	led2.color = (1,0.1,0.35)
	sleep(0.06)

	#.5
	led2.color = (1,0,0.55)
	sleep(0.05)

	#green
	led.color = (0,1,0)
	sleep(0.12)

	#.5
	led.color = (0.25,0.83,0)
	sleep(0.05)

	#green
	led2.color = (1,0,1)
	sleep(0.12)

	#.5
	led2.color = (0.75,0.17,1)
	sleep(0.05)

	#lime
	led.color = (0.5,0.75,0)
	sleep(0.06)

	#.5
	led.color = (0.7,0.83,0)
	sleep(0.05)

	#lime
	led2.color = (0.5,0.25,1)
	sleep(0.06)

	#.5
	led2.color = (0.3,0.17,1)
	sleep(0.05)

	#yellow
	led.color = (1,1,0)
	sleep(0.07)

	#.5
	led.color = (0.78,0.5,0)
	sleep(0.05)

	#yellow
	led2.color = (0,0,1)
	sleep(0.07)

	#.5
	led2.color = (0.22,0.5,1)
	sleep(0.05)

	#orange
	led.color = (0.7,0.25,0)
	sleep(0.06)

	#.5
	led.color = (0.9,0.2,0)
	sleep(0.05)

	#orange
	led2.color = (0.3,0.75,1)
	sleep(0.06)

	#.5
	led2.color = (0.1,0.8,1)
	sleep(0.05)