import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresh = 40
    targColor = [40, 217, 200]

    lower_green = np.array(targColor-thresh)
    upper_green = np.array(targColor+thresh)

    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destryAllWindows()
cap.release()
