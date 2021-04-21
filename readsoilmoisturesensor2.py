#!/usr/bin/env python3

import time, signal, sys
sys.path.append('/home/pi/temp/SDL_Adafruit_ADS1x15')

import SDL_Adafruit_ADS1x15 

def signal_handler(signal, frame):
        print( 'You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

ADS1115 = 0x01	# 16-bit ADC

gain = 4096  # +/- 4.096V

sps = 250  # 250 samples per second

# Initialise the ADC using the default mode (use default I2C address)
adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)
while (1):

	# Read channels  in single-ended mode using the settings above

	voltsCh0 = adc.readADCSingleEnded(0, gain, sps) / 1000
	rawCh0 = adc.readRaw(0, gain, sps)
	print ("%d" % (rawCh1))

	sys.exit(0)