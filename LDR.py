from gpiozero import LightSensor

ldr = LightSensor(4)
while True:
	ldr.wait_for_light()
	print("Light detected")
	ldr.wait_for_dark()
	print("Dark detected")
