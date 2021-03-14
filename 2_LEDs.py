import RPi.GPIO as GPIO   # Library to interact with RPi GPIO port
from time import sleep    # Library to allow us to pause (sleep)

# Below is a a Python LIST used to keep track of which GPIO pins 
#  have an LED attached to them
# A LIST is a way of storing data.
# Lists are ordered, changeable, and allow duplicate values.
# The items are indexed.  That means you can ask for a specific entry.
# They are "zero indexed" which means that the first entry is #0.  The second is #1, etc..
# These notes were summarized from https://www.w3schools.com/python/python_lists.asp
led_pins = [17, 27, 22]

# Below sets GPIO code to use the Broadcom chip-specific numbering on the board for the pins.
# You always have to set the mode.
GPIO.setmode(GPIO.BCM)

# We now iterate through each element in the LIST
# This sets them to be used as an output - we can turn voltage on and off
for led in led_pins:
	GPIO.setup(led, GPIO.OUT)
	
# A variable to store the loop_count
loop_count = 0

# We now create a loop with a while statement.
# We will make all 3 lights cycle 3 times
while loop_count < 3:
	for led in led_pins:		# This walks through all the pins
		GPIO.output(led, True)	# Turn this pin/LED on
		sleep(.3)
		GPIO.output(led, False)	# Turn this pin/LED off
	sleep(1)
	loop_count = loop_count + 1
