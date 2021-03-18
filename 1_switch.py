import RPi.GPIO as GPIO   # Library to interact with RPi GPIO port
from time import sleep    # Library to allow us to pause (sleep)

# Below is a a Python LIST used to keep track of which GPIO pins we are 
#  watching
# A LIST is a way of storing data.
# Lists are ordered, changeable, and allow duplicate values.
# The items are indexed.  That means you can ask for a specific entry.
# They are "zero indexed" which means that the first entry is #0.  The second is #1, etc..
# These notes were summarized from https://www.w3schools.com/python/python_lists.asp
button_pins = [20,21,12,16]

# Below sets GPIO code to use the Broadcom chip-specific numbering on the board for the pins.
# You always have to set the mode.
GPIO.setmode(GPIO.BCM)

# This silences warnings if we didn't exit the last program properly
GPIO.setwarnings(False)

# We now iterate through each element in the LIST
# An input pin floats between 0 and 1 if not connected to voltage
# A pull_up_down supplies voltage so that the pin is has a defined value
#  until it is overrideen by a stronger force.
# We do a "PUD_UP" since we will use a conection with Ground to
#  be what the buttons do.
for button in button_pins:
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Basically setting pin to 1/TRUE

# A variable to store how often a button was pressed
press_count = 0

# We now create a loop with a while statement.
# Until we hae seen 10 button presses we keep looping.
while press_count < 10:
	# Iterate through each pin
	for button in button_pins:
		input_state = GPIO.input(button) # What state is the button in?
		button_position = button_pins.index(button) + 1	# List is zero indexed.
														# So the first button is position 0
		if input_state == False:  # Becomes False if pin connected with Ground/button pressed
			print('Button pressed for pin ' + str(button) + ' which is button ' + str(button_position) + '.')
			sleep(.3) # If we don't sleep - it will look like button got pressed several times
			press_count = press_count + 1  # Increment the press_count variable
		sleep(0.01)  # wait 10 ms to give CPU chance to do other things

# Clean up our GPIO settings
GPIO.cleanup()
# Final message:
print ('Button(s) pressed 10 times.  Bye!')
