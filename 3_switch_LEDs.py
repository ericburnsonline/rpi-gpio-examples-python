from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

led_pins = [13, 19, 20, 21, 26]
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for led in led_pins:
        GPIO.setup(led, GPIO.OUT)

while True:
    input_state = GPIO.input(24)
    if input_state == False:
        print('Button Pressed')
        for led in led_pins:
                GPIO.output(led, True)
                sleep(.2)
                GPIO.output(led, False)
