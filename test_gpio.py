#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

def run():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    while True:
        GPIO.output(26, GPIO.HIGH)
        sleep(0.2)	
        GPIO.output(26, GPIO.LOW)
	sleep(0.2)

if __name__ == "__main__":
   try:
        run()
   except KeyboardInterrupt as e:
        print "\nExiting..."
        GPIO.cleanup()
