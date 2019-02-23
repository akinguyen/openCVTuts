import numpy as np
import cv2

cap = cv2.VideoCapture(0)
convert = cv2.COLOR_BGR2RGB

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(cap.get(3))
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, convert)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
