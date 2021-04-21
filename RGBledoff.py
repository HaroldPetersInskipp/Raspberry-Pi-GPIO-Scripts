#!/usr/bin/env python3

from gpiozero import RGBLED
import time
import sys

led = RGBLED(20,19,21,active_high=True)

led.off()
sleep(1)
sys.exit(0)
