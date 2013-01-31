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
    DIAG_TIME = 0.5
    INTERVAL = 1

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
    
    def engageServos(self, servos):
        self.allPinsDown()
        for servo in servos:
            GPIO.output(servo, True)

        time.sleep(self.INTERVAL) 
        self.allPinsDown()
    def frontLeftUp(self):
        servos = [self.FRONT_LEFT_UP]
        self.engageServos(servos)

    def frontLeftDown(self):
        servos = [self.FRONT_LEFT_DOWN]
        self.engageServos(servos)

    def frontRightUp(self):
        servos = [self.FRONT_RIGHT_UP];
        self.engageServos(servos)

    def frontRightDown(self):
        servos = [self.FRONT_RIGHT_DOWN]
        self.engageServos(servos)

    def rearLeftUp(self):
        servos = [self.REAR_LEFT_UP]
        self.engageServos(servos)

    def rearLeftDown(self):
        servos = [self.REAR_LEFT_DOWN]
        self.engageServos(servos)

    def rearRightUp(self):
        servos = [self.REAR_RIGHT_UP]
        self.engageServos(servos)

    def rearRightDown(self):
        servos = [self.REAR_RIGHT_DOWN]
        self.engageServos(servos)

    def allUp(self):
        servos = [
            self.FRONT_LEFT_UP,
            self.FRONT_RIGHT_UP,
            self.REAR_LEFT_UP,
            self.REAR_RIGHT_UP
        ]
        self.engageServos(servos)

    def allDown(self):
        servos = [
            self.FRONT_LEFT_DOWN,
            self.FRONT_RIGHT_DOWN,
            self.REAR_LEFT_DOWN,
            self.REAR_RIGHT_DOWN
        ]
        self.engageServos(servos)

    def frontUp(self):
        servos = [
            self.FRONT_LEFT_UP,
            self.FRONT_RIGHT_UP
        ]
        self.engageServos(servos)

    def frontDown(self):
        servos = [
            self.FRONT_LEFT_DOWN,
            self.FRONT_RIGHT_DOWN
        ]
        self.engageServos(servos)

    def rearUp(self):
        servos = [
            self.REAR_LEFT_UP,
            self.REAR_RIGHT_UP
        ]
        self.engageServos(servos)

    def rearDown(self):
        servos = [
            self.REAR_LEFT_DOWN,
            self.REAR_RIGHT_DOWN
        ]
        self.engageServos(servos)

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
