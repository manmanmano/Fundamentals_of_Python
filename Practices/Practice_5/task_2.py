import cv2
img = cv2.imread('Images/mynoisy.jpg')
result = cv2.fastNlMeansDenoisingColored(img, None, 12, 10, 7, 21)
cv2.imshow('Original Image', img)
cv2.imshow('Noise removed', result)
cv2.waitKey(0)
