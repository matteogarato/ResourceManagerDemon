import RPi.GPIO as GPIO
import ApiCaller
import time

class GateOpener(object):
    """description of class"""
    RELAIS_1_GPIO = 17
    OPEN_INTERVAL = 3
    ApiCallerInstance = ApiCaller.ApiCaller("")

    def __init__(self, GpioPin, openInterval,baseUrlForCall):
        self.RELAIS_1_GPIO = GpioPin
        OPEN_INTERVAL = openInterval
        ApiCallerInstance = ApiCaller.ApiCaller(baseUrlForCall)
        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

    def Open(readedCode):
        result = ApiCaller.ApiCaller.callCardVerificationApi(readedCode)
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
        time.sleep(OPEN_INTERVAL)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # off


