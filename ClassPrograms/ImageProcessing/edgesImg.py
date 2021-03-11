import cv2
img = cv2.imread('/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/sun.jpg')
edge_img = cv2.Canny(img, 100, 200)
cv2.imshow('Detected edges', edge_img)
cv2.waitKey(5000)
