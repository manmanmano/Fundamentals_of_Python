import cv2
img = cv2.imread("/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/sun.jpg")
rotationMatrix = cv2.getRotationMatrix2D((284/2,177/2),90,.5)
rotatedImage = cv2.warpAffine(img,rotationMatrix,(284,177)) 
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)

