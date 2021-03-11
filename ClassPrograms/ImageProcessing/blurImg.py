import cv2
img = cv2.imread("/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/sun.jpg")
blur_image = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Original image', img)
cv2.imshow('Blur image', blur_image)
cv2.waitKey(5000)
