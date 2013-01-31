import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
DEBUG = 1

class suspension:

    # Define our GPIO pins
    FRONT_LEFT_UP       = 25 
    FRONT_LEFT_DOWN     = 24
    FRONT_RIGHT_UP      = 23
    FRONT_RIGHT_DOWN    = 18
    REAR_LEFT_UP        = 22
    REAR_LEFT_DOWN      = 17
    REAR_RIGHT_UP       = 4
    REAR_RIGHT_DOWN     = 11

    # Duration in seconds before shutting off servos
    DIAG_TIME = 1

    def __init__(self):
        print("initialized")

        # Initialize GPIO pins
        GPIO.setup(self.FRONT_LEFT_UP, GPIO.OUT)
        GPIO.setup(self.FRONT_LEFT_DOWN, GPIO.OUT)
        GPIO.setup(self.FRONT_RIGHT_UP, GPIO.OUT)
        GPIO.setup(self.FRONT_RIGHT_DOWN, GPIO.OUT)
        GPIO.setup(self.REAR_LEFT_UP, GPIO.OUT)
        GPIO.setup(self.REAR_LEFT_DOWN, GPIO.OUT)
        GPIO.setup(self.REAR_RIGHT_UP, GPIO.OUT)
        GPIO.setup(self.REAR_RIGHT_DOWN, GPIO.OUT)

        self.allPinsDown()

    def allPinsDown(self):
        GPIO.output(self.FRONT_LEFT_UP, False)
        GPIO.output(self.FRONT_LEFT_DOWN, False)
        GPIO.output(self.FRONT_RIGHT_UP, False)
        GPIO.output(self.FRONT_RIGHT_DOWN, False)
        GPIO.output(self.REAR_LEFT_UP, False)
        GPIO.output(self.REAR_LEFT_DOWN, False)
        GPIO.output(self.REAR_RIGHT_UP, False)
        GPIO.output(self.REAR_RIGHT_DOWN, False)
    
    def allPinsDownTimed(self):
        time.sleep(DIAG_TIME)

    def frontLeftUp(self):
        GPIO.output(self.FRONT_LEFT_UP, True)
        GPIO.output(self.FRONT_LEFT_DOWN, False)

    def frontLeftDown(self):
        GPIO.output(self.FRONT_LEFT_UP, False)
        GPIO.output(self.FRONT_LEFT_DOWN, True)

    def frontRightUp(self):
        GPIO.output(self.FRONT_LEFT_DOWN, False)
        GPIO.output(self.FRONT_RIGHT_UP, True)

    def frontRightDown(self):
        GPIO.output(self.FRONT_RIGHT_UP, False)
        GPIO.output(self.FRONT_RIGHT_DOWN, True)

    def rearLeftUp(self):
        GPIO.output(self.FRONT_RIGHT_DOWN, False)
        GPIO.output(self.REAR_LEFT_UP, True)

    def rearLeftDown(self):
        GPIO.output(self.REAR_LEFT_UP, False)
        GPIO.output(self.REAR_LEFT_DOWN, True)

    def rearRightUp(self):
        GPIO.output(self.REAR_LEFT_DOWN, False)
        GPIO.output(self.REAR_RIGHT_UP, True)

    def rearRightDown(self):
        GPIO.output(self.REAR_RIGHT_UP, False)
        GPIO.output(self.REAR_RIGHT_DOWN, True)

    def allUp(self):
        self.frontUp()
        self.rearUp()

    def allDown(self):
        self.frontDown()
        self.rearDown()

    def frontUp(self):
        self.frontLeftUp()
        self.frontRightUp()

    def frontDown(self):
        self.frontLeftDown()
        self.frontRightDown()

    def rearUp(self):
        self.rearLeftUp()
        self.rearRightUp()

    def rearDown(self):
        self.rearLeftDown()
        self.rearRightDown()

    def diagnostic(self):
        while (True):
            print("Front Left Up")
            self.frontLeftUp()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Front Left Down")
            self.frontLeftDown()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Front Right Up")
            self.frontRightUp()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Front Right Down")
            self.frontRightDown()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Rear Left Up")
            self.rearLeftUp()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Rear Left Down")
            self.rearLeftDown()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Rear Right Up")
            self.rearRightUp()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Rear Right Down")
            self.rearRightDown()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Front Up")
            self.frontUp()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Front Down")
            self.frontDown()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("Rear Up")
            self.rearUp()
            time.sleep(self.DIAG_TIME)
        
            self.allPinsDown()

            print("Rear Down")
            self.rearDown()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("All Up")
            self.allUp()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()

            print("All Down")
            self.allDown()
            time.sleep(self.DIAG_TIME)

            self.allPinsDown()
