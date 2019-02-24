import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel1 = np.ones((15, 15), np.uint8)/255
kernel2 = np.ones((20, 20), np.uint8)/400


def filter(hsv, lower, upper, kernel1, kernel2):
    # removing background noise
    mask = cv2.inRange(hsv, lower, upper)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1)
    # removing inner noise inside object
    return cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel2)


def filterErosion(hsv, lower, upper, kernel1, kernel2):
    # removing background noise
    mask = cv2.inRange(hsv, lower, upper)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1)
    # removing inner noise inside object
    return opening


def filterDilation(hsv, lower, upper, kernel1, kernel2):
    # removing background noise
    mask = cv2.inRange(hsv, lower, upper)
    opening = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel1)
    # removing inner noise inside object
    return opening


def getColorBound(b, g, r, lowDiff, upperDiff):
    color = np.uint8([[[b, g, r]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    lower_color = np.array([hsv_color[0][0][0] - lowDiff, 100, 100])
    upper_color = np.array([hsv_color[0][0][0] + upperDiff, 255, 255])
    return lower_color, upper_color


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


lower_blue = np.array([90, 80, 55])
upper_blue = np.array([130, 255, 255])


lower_green, upper_green = [(39, 80, 40), (90, 255, 255)]
#lower_green, upper_green = getColorBound(0, 255, 0, 10, 50)
# getColorBound(0, 2, 255, 50, 8)
lower_red, upper_red = [(0, 90, 50), (8, 255, 255)]

lower_white = np.array([80, 55, 100])
upper_white = np.array([130, 79, 255])

lower_orange, upper_orange = getColorBound(0, 165, 255, 12, 5)

lower_yellow, upper_yellow = getColorBound(0, 255, 255, 10, 10)

while True:
    ret, frame = cap.read()
    blur = cv2.GaussianBlur(frame, (19, 19), 0)
    median = cv2.medianBlur(blur, 5)
    # Reducing noises
    hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = np.multiply(hsv[:, :, 2], 0.60, casting='unsafe')
    test = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("test", test)
    cv2.imshow("original", frame)

    # Create color mask
    mask_blue = filter(hsv, lower_blue, upper_blue, kernel1, kernel2)
    mask_green = filter(hsv, lower_green, upper_green, kernel1, kernel2)
    mask_orange = filter(hsv, lower_orange, upper_orange, kernel1, kernel2)
    mask_yellow = filter(hsv, lower_yellow, upper_yellow, kernel1, kernel2)
    mask_red = filter(hsv, lower_red, upper_red, kernel1, kernel2)
    mask_white = filter(hsv, lower_white, upper_white, kernel1, kernel2)

    # Create color contours
    contoursBlue, h = cv2.findContours(
        mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contoursGreen, h = cv2.findContours(
        mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contoursOrange, h = cv2.findContours(
        mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contoursYellow, h = cv2.findContours(
        mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contoursRed, h = cv2.findContours(
        mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contoursWhite, h = cv2.findContours(
        mask_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    drawContours("blue", contoursBlue)
    drawContours("orange", contoursOrange)
    drawContours("green", contoursGreen)
    drawContours("yellow", contoursYellow)
    drawContours("red", contoursRed)
    drawContours("white", contoursWhite)
    cv2.imshow('detection', frame)

    cv2.imshow("closing", mask_red)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
