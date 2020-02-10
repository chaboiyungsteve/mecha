import RPi.GPIO as GPIO
import time

# set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)


# setup GPIO using Board numbering
# GPIO.setmode(GPIO.BOARD)

# Button Pin Setup
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED Pins Setup
GPIO.setup(18, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

while True:
    if (GPIO.input(4) == 1):
        print("dd")
        time.sleep(.1)
        GPIO.output(18, GPIO.HIGH)
