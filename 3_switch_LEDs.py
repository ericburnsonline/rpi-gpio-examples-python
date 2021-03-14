import RPi.GPIO as GPIO   # Library to interact with RPi GPIO port
from time import sleep    # Library to allow us to pause (sleep)

# Below is a a Python LIST used to keep track of which GPIO pins 
#  have an LED attached to them
# A LIST is a way of storing data.
# Lists are ordered, changeable, and allow duplicate vallues.
# The items are indexed.  That means you can ask for a specific entry.
# They are "zero indexed" which means that the first entry is #0.  The second is #1, etc..
# These notes were summarized from https://www.w3schools.com/python/python_lists.asp
led_pins = [17, 27, 22]

# Below is a a Python LIST used to keep track of which GPIO pins we are 
#  watching
button_pins = [18, 12, 24, 23]

# Below sets GPIO code to use the Broadcom chip-specific numbering on the board for the pins.
# You always have to set the mode.
GPIO.setmode(GPIO.BCM)

# We now iterate through each element in the LIST
# An input pin floats between 0 and 1 if not connected to voltage
# A pull_up_down supplies voltage so that the pin is has a defined value
#  until it is overrideen by a stronger force.
# We do a "PUD_UP" since we will use a conection with Ground to
#  be what the buttons do.
for button in button_pins:
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Basically setting pin to 1/TRUE


#GPIO.setwarnings(False)

# We now iterate through each element in the LIST
# This sets them to be used as an output - we can turn voltage on and off
for led in led_pins:
        GPIO.setup(led, GPIO.OUT)

button4pressed = False

while not button4pressed:
        for button in button_pins:
                input_state = GPIO.input(button) # What state is the button in?
		button_position = button_pins.index(button) + 1	# List is zero indexed.
														# So the first button is position 0
                if input_state == False:  # Becomes False if pin connected 
                                        # with Ground/button pressed
                        # If pin is 1-3, then turn on light, pause and off
                        if button_position < 4:
                                print('Button pressed for pin ' + str(button) + ' which is button ' + str(button_position) + '.')
                                led = button_position - 1 # Get correct entry in List
                                GPIO.output(led_pins[button_position-1], True)	# Turn this pin/LED on
                                sleep(.3)
                                GPIO.output(led_pins[button_position-1], False)	# Turn this pin/LED off
                                sleep(.3) # If we don't sleep - it will look like button got pressed several times
                        # If pin is 4, then exit
                        if button_position == 4:
                                print('Button 4 pressed, time to exit!')
                                # EXIT!
                                button4pressed = True
                        
                        sleep(0.01)  # wait 10 ms to give CPU chance to do other things

# Final message:
print ('Button 4 pressed.  Bye!')
