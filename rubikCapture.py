import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))
while True:
    ret, frame = cap.read()
    w, h = (20, 20)
    rectCoordinates = [(200, 200), (260, 200), (320, 200),
                       (200, 260), (260, 260), (320, 260),
                       (200, 320), (260, 320), (320, 320)]

    for coord in rectCoordinates:
        cv2.rectangle(
            frame, coord, (coord[0]+w, coord[1]+h), (147, 20, 255), -1)

    cv2.imshow("video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("images/rubikCapture.jpg", frame)


cap.release()
cv2.destroyAllWindows()
