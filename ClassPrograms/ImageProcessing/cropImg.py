import cv2
img = cv2.imread("/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/sun.jpg")
startRow = int(177*.15)
startCol = int(284*.15)
endRow = int(177*.85)
endCol = int(284*85)
croppedImage = img[startRow:endRow, startCol:endCol]
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', croppedImage)
cv2.waitKey(0)
