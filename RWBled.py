from gpiozero import LED
from time import sleep

red = LED(18)
white = LED(19)
blue = LED(21)

while True:
	red.on()
	sleep(1)
	red.off()
	sleep(1)
	white.on()
	sleep(1)
	white.off()
	sleep(1)
	blue.on()
	sleep(1)
	blue.off()
	sleep(1)
