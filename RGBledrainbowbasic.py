#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(20,19,21,active_high=True)

while True:
	#Red pin 20
	led.color = (1,0,0)
	sleep(0.6)
	led.off()

	#Green pin 19
	led.color = (0,1,0)
	sleep(0.6)
	led.off()

	#Pink pins 20, 19, and 21
	led.color = (1,0.35,0.35)
	sleep(0.6)
	led.off()

	#Blue pin 21
	led.color = (0,0,1)
	sleep(0.6)
	led.off()

	#Yellow pins 20 and 19
	led.color = (1,1,0)
	sleep(0.6)
	led.off()

	#Purple pins 20 and 21
	led.color = (1,0,1)
	sleep(0.6)
	led.off()

	#Orange pins 20 and 19
	led.color = (1,0.25,0)
	sleep(0.6)
	led.off()

	#??? pins 20, 19 and 21
	led.color = (0.5,0.2,0.6)
	sleep(0.6)
	led.off()

	#Cyan pins 19 and 21
	led.color = (0,1,0.9)
	sleep(0.6)
	led.off()
