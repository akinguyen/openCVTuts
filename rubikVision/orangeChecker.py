import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as colors


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
kernel1 = np.ones((15, 15), np.uint8)/255
kernel2 = np.ones((20, 20), np.uint8)/400


def filter(hsv, lower, upper, kernel1, kernel2):
    # removing background noise
    mask = cv2.inRange(hsv, lower, upper)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1)
    # removing inner noise inside object
    return cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel2)


def drawContours(color, contours):
    for i in range(len(contours)):

        # Unoptimized border
        x, y, w, h = cv2.boundingRect(contours[i])

        # Optimized border
        rect = cv2.minAreaRect(contours[i])
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        im = cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
        cv2.putText(frame, color, (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)


cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower, upper)
    contoursRed, h = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #mask_filter = filter(hsv, lower, upper, kernel1, kernel2)
    drawContours("red", contoursRed)
    mask_filter = cv2.medianBlur(mask, 5)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
