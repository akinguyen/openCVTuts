import cv2
import numpy as np

kernel1 = np.ones((15, 15), np.uint8)/255
kernel2 = np.ones((20, 20), np.uint8)/400


def getColorBound(b, g, r, lowDiff, upperDiff):
    color = np.uint8([[[b, g, r]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    lower_color = np.array([hsv_color[0][0][0] - lowDiff, 100, 100])
    upper_color = np.array([hsv_color[0][0][0] + upperDiff, 255, 255])
    return lower_color, upper_color


def storeInDataSet(kernel1, kernel2):
    rubik = cv2.imread("dataset/temp/rubikFilter.jpg")
    originalImage = cv2.imread("dataset/temp/rubikCapture.jpg")
    hsv = cv2.cvtColor(rubik, cv2.COLOR_BGR2HSV)
    lower_pink, upper_pink = getColorBound(147, 29, 255, 1, 1)
    mask_pink = filter(hsv, lower_pink, upper_pink, kernel1, kernel2)
    contoursPink, h = cv2.findContours(
        mask_pink, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rubik = cv2.bitwise_and(originalImage, originalImage, mask=mask_pink)
    cv2.imshow(rubik)


cap = cv2.VideoCapture(0)

rectCoordinates = [(200, 200), (260, 200), (320, 200),
                   (200, 260), (260, 260), (320, 260),
                   (200, 320), (260, 320), (320, 320)]
w, h = (26, 26)
while True:
    ret, frame = cap.read()
    original = frame.copy()
    for coord in rectCoordinates:
        cv2.rectangle(
            frame, coord, (coord[0]+w, coord[1]+h), (147, 20, 255), -1)

    cv2.imshow("video", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("dataset/temp/rubikCapture.jpg", original)
        cv2.imwrite("dataset/temp/rubikFilter.jpg", frame)
        #storeInDataSet(kernel1, kernel2)

cap.release()
cv2.destroyAllWindows()
