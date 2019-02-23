import cv2
import numpy as np


def filterNoise(mask):
    kernel = np.ones((15, 15), np.uint8)/255
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((20, 20), np.uint8)/400
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return closing


def filterImage(image):
    return


rubik = cv2.imread("images/rubik_face.jpg")

hsv = cv2.cvtColor(rubik, cv2.COLOR_BGR2HSV)

# Create color boundaries
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

lower_green = np.array([40, 150, 50])
upper_green = np.array([100, 255, 180])

lower_red = np.array([120, 100, 100])
upper_red = np.array([255, 255, 255])

lower_white = np.array([0, 0, 100])
upper_white = np.array([0, 0, 255])

orange = np.uint8([[[0, 165, 255]]])
hsv_orange = cv2.cvtColor(orange, cv2.COLOR_BGR2HSV)
lower_orange = np.array([hsv_orange[0][0][0] - 10, 100, 100])
upper_orange = np.array([hsv_orange[0][0][0] + 5, 255, 255])

lower_yellow = np.array([hsv_orange[0][0][0] - 5, 100, 100])
upper_yellow = np.array([hsv_orange[0][0][0] + 10, 255, 255])


# Create color mask
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_white = cv2.inRange(hsv, lower_white, upper_white)

# Create color contours
contoursBlue, h = cv2.findContours(
    mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contoursgreen, h = cv2.findContours(
    mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contoursOrange, h = cv2.findContours(
    mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contoursYellow, h = cv2.findContours(
    mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contoursRed, h = cv2.findContours(
    mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contoursWhite, h = cv2.findContours(
    mask_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Blue")
for i in range(len(contoursBlue)):
    x, y, w, h = cv2.boundingRect(contoursBlue[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))

print("Green")
for i in range(len(contoursgreen)):
    x, y, w, h = cv2.boundingRect(contoursgreen[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))

print("Orange")
for i in range(len(contoursOrange)):
    x, y, w, h = cv2.boundingRect(contoursOrange[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))

print("Yellow")
for i in range(len(contoursYellow)):
    x, y, w, h = cv2.boundingRect(contoursYellow[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))

print("Red")
for i in range(len(contoursRed)):
    x, y, w, h = cv2.boundingRect(contoursRed[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))

print("White")
for i in range(len(contoursWhite)):
    x, y, w, h = cv2.boundingRect(contoursWhite[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))

cv2.imshow('image', rubik)
cv2.imshow('blue', mask_white)


k = cv2.waitKey(0)
if (k == ord('q')):
    cv2.destroyAllWindows()
