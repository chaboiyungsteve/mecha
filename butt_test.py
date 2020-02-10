import RPi.GPIO as GPIO
import time

# set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Button Pin Setup
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED Pins Setup
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

ledClock = .1
game = True
button = GPIO.input(4)
i = 18

while (game == True and button == 0):
    GPIO.output(i, GPIO.HIGH)
    time.sleep(ledClock)
    GPIO.output(i, GPIO.LOW)
    time.sleep(ledClock)
    i = i+1
    if i == 25:
        i = 18

        # while (game == True and GPIO.input(4) == 0):
        #     for i in range(18, 25):
        #         GPIO.output(i, GPIO.HIGH)
        #         time.sleep(ledClock)
        #         GPIO.output(i, GPIO.LOW)
        #         time.sleep(ledClock)
        #         if (GPIO.input(4) == 1):
        #             GPIO.output(i, GPIO.HIGH)
        #             game = False


GPIO.cleanup()
