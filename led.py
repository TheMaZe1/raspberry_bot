import RPi.GPIO as GPIO
from time import sleep

red_led_pin = 21
GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)      # Use Board pin numbering
GPIO.setup(red_led_pin, GPIO.OUT)

GPIO.output(red_led_pin, True)
sleep(10)
GPIO.output(red_led_pin, False)