import RPi.GPIO as GPIO
import time

class GateOpener(object):
    """description of class"""
    RELAIS_1_GPIO = 17
    OPEN_INTERVAL = 3

    def __init__(self, GpioPin, openInterval):
        self.RELAIS_1_GPIO = GpioPin
        OPEN_INTERVAL = openInterval
        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

    def Open():
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
        time.sleep(OPEN_INTERVAL)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # off


