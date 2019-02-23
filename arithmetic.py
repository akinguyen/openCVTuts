import cv2
import numpy as numpy


trump = cv2.imread("images/trump.jpg", 0)
kim = cv2.imread("images/kim.jpg", 0)
print(kim.shape)
trump = cv2.resize(trump, (220, 262))
# cv2.imshow('trump', trump)

add = cv2.addWeighted(trump, 0.7, kim, 0.3, 0)

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()
