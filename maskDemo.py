import cv2
import numpy as np
from matplotlib import pyplot as plt

kim = cv2.imread("images/kim.jpg")

gray_kim = cv2.cvtColor(kim, cv2.COLOR_BGR2GRAY)

#ret, mask = cv2.threshold(gray_kim, 100, 255, cv2.THRESH_BINARY)
ret, mask = cv2.threshold(gray_kim, 42, 255, cv2.THRESH_BINARY_INV)
#ret, mask = cv2.threshold(gray_kim, 100, 255, cv2.THRESH_TRUNC)

mask_inv = cv2.bitwise_not(mask)
img = cv2.imread("images/deadpool.jpg")
book = cv2.imread("images/bookpage.jpg")

gray_book = cv2.cvtColor(book, cv2.COLOR_BGR2GRAY)

# Clear the dark shade of the bookpage
th2 = cv2.adaptiveThreshold(gray_book, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 11, 2)
r, c = gray_kim.shape
roi = img[0:r, 0: c]

# Any original image part that match the white part of the mask will be kept
# Any black part of the mask will remove the matched part in the original
kim_bg = cv2.bitwise_and(roi, roi, mask=mask)
kim_fg = cv2.bitwise_and(kim, kim, mask=mask_inv)
dst = (kim_bg + kim_fg)
images = [kim_bg, kim_fg, dst, gray_kim, mask, mask_inv, th2]

for i in range(len(images)):
    plt.subplot(2, 4, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB),
               cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow("kim_fg", th2)
#cv2.imshow("kimbg", kim_bg)
#cv2.imshow("kim", gray_kim)
#cv2.imshow("res", dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
