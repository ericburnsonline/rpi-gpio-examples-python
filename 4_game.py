from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep
from time import time
import random

# Version 1.0
# GPIO based version of https://projects.raspberrypi.org/en/projects/lights-out/8

def button_pressed(button, light):
	print("You pressed button " + str(button) + " for light " + str(light) )
	GPIO.output(led_pins[light], False)


#led_pins = [22, 27, 17]
led_pins = [17, 27, 22]
button_pins = [20, 21, 12]

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

# We now iterate through each element in the LIST
# This sets them to be used as an output - we can turn voltage on and off
for led in led_pins:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, False)  #turn them all off

# Keep playing the game until game_in_progres becomes False
game_in_progress = True
TIME_ALLOWED = 1.5
score = 0
fastest_time = 99

waiting_for_press = True

while waiting_for_press and game_in_progress:
	waiting_for_press = True
	print('Get Ready!')
	# Randomly choose the number of a light (1-3)
	light = random.randint(1,3)

	wait_for_next = random.uniform(0.5, 3.5)
	sleep(wait_for_next)

	GPIO.output(led_pins[light-1], True)
	start = time()

	while waiting_for_press:
		now = time()
		# We watch the buttons.
		for button in button_pins:
			input_state = GPIO.input(button)    # What state is the button in?
			n = button_pins.index(button) + 1	# List is zero indexed.
  						                        # So the first button is position 0
			if input_state == False:    # Becomes False if pin connected 
        				                # with Ground/button pressed
				waiting_for_press = False
				time_taken = now - start
				if (time_taken < fastest_time):
					fastest_time = time_taken

				if time_taken > TIME_ALLOWED:
					print('You took too long!')
					# Turn off light
					game_in_progress = False
				if (light == n):
					print("Correct!")
					score = score + 1
				else:
					print("Wrong - it was " + str(light)) + " and you pressed " + str(n)
					game_in_progress = False	
	waiting_for_press = True
	GPIO.output(led_pins[light-1], False)
	TIME_ALLOWED = TIME_ALLOWED * 0.99
	print('New Time Allowed is ' + str(TIME_ALLOWED))

# Let's flash them all to let person know they lost
count = 0
while count < 3:
	for led in led_pins:
		GPIO.output(led, True)  #turn them all off
	sleep(.5)
	for led in led_pins:
		GPIO.output(led, False)  #turn them all off
	sleep(.2)
	count = count + 1

print('Sorry, game over!')
print('You scored ' + str(score) + ' and time allowed per round was down to ' + str(TIME_ALLOWED))
if (score > 0):
	print('Your fastest time was ' + str(fastest_time))
