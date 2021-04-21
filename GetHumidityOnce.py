import time
import board
import adafruit_si7021
import sys

sensor = adafruit_si7021.SI7021(board.I2C())

print("%0.1f" % sensor.relative_humidity)
sys.exit(0)
