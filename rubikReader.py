import cv2
import numpy as np


def filter(hsv, lower, upper, kernel1, kernel2):
    # removing background noise
    mask = cv2.inRange(hsv, lower, upper)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1)
    # removing inner noise inside object
    return cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel2)


def getColorBound(b, g, r, lowDiff, upperDiff):
    color = np.uint8([[[b, g, r]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    lower_color = np.array([hsv_color[0][0][0] - lowDiff, 100, 100])
    upper_color = np.array([hsv_color[0][0][0] + upperDiff, 255, 255])
    return lower_color, upper_color


def getColorPosition(x, y):
    if ((x >= 200 and x <= 226) and (y >= 200 and y <= 226)):
        rubikString.insert(0, "blue")


kernel1 = np.ones((15, 15), np.uint8)/255
kernel2 = np.ones((20, 20), np.uint8)/400
rubik = cv2.imread("images/rubikFilter.jpg")


originalImage = cv2.imread("images/rubikCapture.jpg")

hsv = cv2.cvtColor(rubik, cv2.COLOR_BGR2HSV)
lower_pink, upper_pink = getColorBound(147, 29, 255, 1, 1)
mask_pink = filter(hsv, lower_pink, upper_pink, kernel1, kernel2)
contoursPink, h = cv2.findContours(
    mask_pink, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rubik = cv2.bitwise_and(originalImage, originalImage, mask=mask_pink)

blur = cv2.GaussianBlur(rubik, (19, 19), 0)
median = cv2.medianBlur(blur, 5)
# Reducing noises
hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
hsv[:, :, 2] = np.multiply(hsv[:, :, 2], 0.65, casting='unsafe')
# detect color of the original image


lower_blue = np.array([90, 80, 55])
upper_blue = np.array([130, 255, 255])


lower_green, upper_green = [(39, 80, 40), (90, 255, 255)]
#lower_green, upper_green = getColorBound(0, 255, 0, 10, 50)
# getColorBound(0, 2, 255, 50, 8)
lower_red, upper_red = [(0, 90, 50), (8, 255, 255)]

lower_white, upper_white = [(80, 0, 100), (130, 79, 255)]

lower_orange, upper_orange = getColorBound(0, 165, 255, 12, 5)

lower_yellow, upper_yellow = getColorBound(0, 255, 255, 10, 10)

# Create color mask
mask_blue = filter(hsv, lower_blue, upper_blue, kernel1, kernel2)
mask_green = filter(hsv, lower_green, upper_green, kernel1, kernel2)
mask_orange = filter(hsv, lower_orange, upper_orange, kernel1, kernel2)
mask_yellow = filter(hsv, lower_yellow, upper_yellow, kernel1, kernel2)
mask_red1 = filter(hsv, lower_red, upper_red, kernel1, kernel2)
mask_red2 = filter(hsv, (166, 100, 100), (180, 255, 255), kernel1, kernel2)
mask_red = mask_red1 + mask_red2
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

rubikString = []
print("Blue")
for i in range(len(contoursBlue)):
    x, y, w, h = cv2.boundingRect(contoursBlue[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))
    print(w, h)


print("Green")
for i in range(len(contoursGreen)):
    x, y, w, h = cv2.boundingRect(contoursGreen[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))
    print(w, h)

print("Orange")
for i in range(len(contoursOrange)):
    x, y, w, h = cv2.boundingRect(contoursOrange[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))
    print(w, h)

print("Yellow")
for i in range(len(contoursYellow)):
    x, y, w, h = cv2.boundingRect(contoursYellow[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))
    print(w, h)

print("Red")
for i in range(len(contoursRed)):
    x, y, w, h = cv2.boundingRect(contoursRed[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))
    print(w, h)

print("White")
for i in range(len(contoursWhite)):
    x, y, w, h = cv2.boundingRect(contoursWhite[i])
    cv2.rectangle(rubik, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("x = {0}, y = {1}".format(x, y))
    print(w, h)


cv2.imshow('image', rubik)
cv2.imshow('blue', mask_orange)


k = cv2.waitKey(0)
if (k == ord('q')):
    cv2.destroyAllWindows()
