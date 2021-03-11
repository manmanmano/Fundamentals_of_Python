import cv2
img = cv2.imread("/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/sun.jpg")
newImg = cv2.resize(img, (550, 350))
cv2.imshow('Resized Image', newImg)
cv2.waitKey(0)
