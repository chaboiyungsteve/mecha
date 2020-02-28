import RPi.GPIO as GPIO
import time

# set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Button Pin Setup
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.LOW)

# LED Pins Setup
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    ledClock = .1
    game = True
    i = 18

    while (game == True):
        GPIO.output(i, GPIO.HIGH)
        time.sleep(ledClock)
        GPIO.output(i, GPIO.LOW)
        time.sleep(ledClock)
        i = i+1
        if i == 25:
            i = 18
        if GPIO.output(5) == 1:
            GPIO.output(i, GPIO.HIGH)
            game = False
   
   
    GPIO.output(21, GPIO.HIGH)
    time.sleep(ledClock)
    GPIO.output(21, GPIO.LOW)
    time.sleep(ledClock)
    GPIO.output(21, GPIO.HIGH)        
    print("You win")
    time.sleep(3)
    GPIO.output(21, GPIO.LOW)

    GPIO.cleanup()
