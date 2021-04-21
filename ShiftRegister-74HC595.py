#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from sys import version_info

if version_info.major == 3:
	raw_input = input

SDI   = 17
RCLK  = 18
SRCLK = 27

#===============   LED Mode Define ================
#   You can define yourself, in binary, and convert it to Hex
#   8 bits a group, 0 means off, 1 means on
#   like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#   and convert to 0x55.

BLINK = [0x00,0x3f,0x1f,0x0f,0x07,0x03,0x01,0x00]
LED0 = [0x00,0x01,0x03,0x07,0x0f,0x1f,0x3f,0x00]
LED1 = [0x00,0x09,0x00,0x12,0x00,0x24,0x00,0x3f]
LED2 = [0x00,0x1b,0x36,0x2d,0x1b,0x36,0x2d,0x00]
#=================================================

def print_message():
    print ("==============================")
    print ("|      LEDs with 74HC595     |")
    print ("|----------------------------|")
    print ("|    SDI connect to GPIO17   |")
    print ("|    RCLK connect to GPIO18  |")
    print ("|   SRCLK connect to GPIO27  |")
    print ("|  Control LEDs with 74HC595 |")
    print ("==============================")
    print ("Program is running...")
    print ("Please press Ctrl+C to end the program..")
    raw_input ("Press Enter to begin\n")

def setup():
    GPIO.setmode(GPIO.BCM)    # Number GPIOs by its BCM location
    GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)

# Shift the data to 74HC595
def hc595_shift(dat):
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def main():
    print_message()
    mode = LED2 # Change Mode, modes from LED0 to LED3
    sleeptime = 0.25        # Change speed, lower value, faster speed
    blink_sleeptime = 0.25
    leds = ['-', '-', '-', '-', '-', '-', '-', '-']
    while True:
        # Change LED status from mode
        print ("  mode  ")
        for onoff in mode:
            hc595_shift(onoff)
            leds[mode.index(onoff)] = 1    # Show which led is on
            print (leds)
            time.sleep(sleeptime)
            leds[mode.index(onoff)] = '-'  # Show the led is off

        # Change LED status from mode reverse
        print ("  reversed mode  ")
        for onoff in reversed(mode):
            hc595_shift(onoff)
            leds[mode.index(onoff)] = 1    # Show which led is on
            print (leds)
            time.sleep(sleeptime)
            leds[mode.index(onoff)] = '-'  # Show the led is off

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
