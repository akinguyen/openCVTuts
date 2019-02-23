import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("images/deadpool.jpg", 0)

'''
#display image by matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
# to hide tick values on X and Y axis
plt.xticks([1, 9, 1]), plt.yticks([1, 9, 1])
plt.show()

'''
cv2.imshow('image', img)
k = cv2.waitKey(0)
if (k == 1):
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("images/test.jpg", img)
    cv2.destroyAllWindows()
