import RPi.GPIO as GPIO
import time

# set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)


# setup GPIO using Board numbering
# GPIO.setmode(GPIO.BOARD)

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

while True:
    for i in range(18, 25):
        GPIO.output(i, GPIO.HIGH)
        time.sleep(ledClock)
        GPIO.output(i, GPIO.LOW)
        time.sleep(ledClock)
    if (GPIO.input(4) == 1):
        break
        GPIO.output(i, GPIO.HIGH)
    GPIO.cleanup()
