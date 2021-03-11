import cv2
img = cv2.imread("/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/Finger.png")
blur_image = cv2.medianBlur(img, 5)
cv2.imshow('Original image', img)
cv2.imshow('Blur image', blur_image)
cv2.waitKey(5000)

