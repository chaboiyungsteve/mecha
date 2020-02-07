import RPi.GPIO as GPIO

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)


#setup GPIO using Board numbering
#GPIO.setmode(GPIO.BOARD)

GPIO.setup(4, GPIO.IN, buttSignal = GPIO.PUD_DOWN)

while True:
    if (GPIO.input(4) == 1):
        print("dd")
