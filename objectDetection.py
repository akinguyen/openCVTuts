import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# pen detection
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    orange = np.uint8([[[0, 165, 255]]])
    hsv_orange = cv2.cvtColor(orange, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([hsv_orange[0][0][0] - 9, 100, 100])
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

    kernel = np.ones((15, 15), np.uint8)/255

    # removing background noise
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((20, 20), np.uint8)/400
    # removing inner noise inside object
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    #img = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    resWithoutNoise = cv2.bitwise_and(frame, frame, mask=closing)
    contours, h = cv2.findContours(
        closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[0])

        # Unoptimized border
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Optimized border
        rect = cv2.minAreaRect(contours[i])
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        im = cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

    #frame = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    cv2.imshow('frame', frame)
    cv2.imshow('res', resWithoutNoise)
    cv2.imshow("closing", closing)
    #cv2.imshow("img", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
