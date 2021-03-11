import cv2
import numpy as np
img = cv2.imread("/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/sun.jpg")
contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
cv2.imshow('Original image', img)
cv2.imshow('Contrast image', contrast_img)
cv2.waitKey(3000)

