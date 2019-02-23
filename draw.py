import numpy as np
import cv2

# Create a black image
img = np.ones((512, 512, 3), np.uint8)
img1 = cv2.imread("images/deadpool.jpg")
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img1, (400, 400), (500, 400), (255, 0, 0), 3)
cv2.putText(img1, "Open CV tuts!", (200, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.rectangle(img, (0, 0), (510, 128), (0, 255, 0), 3)

print(img1.shape)
eye = img1[280:430, 340:500]
x = 430 - 280
y = 500 - 340
img1[0:x, 0:y] = eye
b, g, r = cv2.split(img)
img[:, :, 2] = 1
cv2.imshow("draw", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
