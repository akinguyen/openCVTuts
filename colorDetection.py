import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    orange = np.uint8([[[0, 165, 255]]])
    hsv_orange = cv2.cvtColor(orange, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([hsv_orange[0][0][0] - 10, 100, 100])
    upper_orange = np.array([hsv_orange[0][0][0] + 50, 255, 255])

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_red = np.array([11, 50, 50])  # example value
    upper_red = np.array([20, 255, 255])  # example value

    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # White = 1, black = 0
    #mask = mask_blue + mask_red + mask_orange
    mask = mask_blue
    res = cv2.bitwise_and(frame, frame, mask=mask)

    blur = cv2.GaussianBlur(res, (15, 15), 0)
    mean = cv2.medianBlur(res, 9)
    kernel = np.ones((15, 15), np.uint8)/255

    # removing background noise
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # removing inner noise inside object
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    resWithoutNoise = cv2.bitwise_and(frame, frame, mask=closing)

    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mean', mean)
    cv2.imshow('res', resWithoutNoise)
    cv2.imshow("opening", opening)
    cv2.imshow("closing", closing)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
