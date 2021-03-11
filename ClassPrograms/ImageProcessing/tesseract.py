import pytesseract as tess
import cv2
img = cv2.imread('/home/jimi/Documents/TalTech/Md/IntroToPython/Practice_5/Images/file.jpg')
text = tess.image_to_string(img)
print(text)
