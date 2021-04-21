#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

red = LED(20,active_high=True)
yellow = LED(18,active_high=True)
green = LED(19,active_high=True)
blue = LED(21,active_high=True)
white = LED(26,active_high=True)

while True:
