import cv2
img = cv2.imread('/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/sun.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image', img)
cv2.imshow('Gray Scale Image', gray_img)
cv2.waitKey(5000)

