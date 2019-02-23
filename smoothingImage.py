import cv2
import numpy as np
from matplotlib import pyplot as plt

book = cv2.imread("images/bookpage.jpg")

gray_book = cv2.cvtColor(book, cv2.COLOR_BGR2GRAY)

gray_book = cv2.adaptiveThreshold(gray_book, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 11, 2)

blur = cv2.GaussianBlur(book, (5, 5), 0)
gray_book_blur = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
gray_book_blur = cv2.adaptiveThreshold(
    gray_book, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)


plt.subplot(121), plt.imshow(gray_book), plt.title("Original")
plt.xticks([]), plt.yticks([])

plt.subplot(121), plt.imshow(gray_book_blur), plt.title("Blur")
plt.xticks([]), plt.yticks([])

kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(cv2.bitwise_not(gray_book), cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(cv2.bitwise_not(gray_book), cv2.MORPH_CLOSE, kernel)

cv2.imshow("b", book)
cv2.imshow("c", opening)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
