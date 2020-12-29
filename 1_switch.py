import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
press_count = 0

while True:
  input_state = GPIO.input(24)
    if input_state == False:
	press_count = press_count + 1
  if (press_count == 1):
    print('Button pressed once.')
  else:
    print('Button pressed ' + str(press_count) + ' times.')
    sleep(0.3)	
