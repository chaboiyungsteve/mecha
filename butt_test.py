import RPi.GPIO as GPIO
import time

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)


#setup GPIO using Board numbering
#GPIO.setmode(GPIO.BOARD)

GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if (GPIO.input(4) == 1):
        print("dd")
        time.sleep(3)
