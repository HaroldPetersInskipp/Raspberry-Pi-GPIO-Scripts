#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(18,19,21,active_high=True)

while True:
        #Red
        led.color = (1,0,0)
        sleep(1)
        led.off()
        #Green
        led.color = (0,1,0)
        sleep(1)
        led.off()
        #Blue
        led.color = (0,0,1)
        sleep(1)
        led.off()
        #Purple
        led.color = (1,0,1)
        sleep(1)
        led.off()
        #Yellow
        led.color = (1,1,0)
        sleep(1)
        led.off()
        #White
        led.color = (1,1,1)
        sleep(1)
        led.off()
        #Cyan
        led.color = (0,1,1)
        sleep(1)
        led.off()