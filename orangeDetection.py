import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    orange = np.uint8([[[0, 165, 255]]])
    hsv_orange = cv2.cvtColor(orange, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([hsv_orange[0][0][0] - 8, 100, 100])
    upper_orange = np.array([hsv_orange[0][0][0] + 2, 255, 255])

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_red = np.array([11, 50, 50])  # example value
    upper_red = np.array([20, 255, 255])  # example value

    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # White = 1, black = 0
    #mask = mask_blue + mask_red + mask_orange
    mask = mask_orange
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

        # Unoptimized border
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Optimized circular border
        (x, y), radius = cv2.minEnclosingCircle(contours[i])
        center = (int(x), int(y))
        radius = int(radius)
        img = cv2.circle(frame, center, radius, (0, 255, 0), 2)
        cv2.putText(frame, "orange", center,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

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
