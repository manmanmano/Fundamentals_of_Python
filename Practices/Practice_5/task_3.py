import pytesseract as tess
import cv2
img = cv2.imread('Images/linusquote.jpg')
text = tess.image_to_string(img)
print(text)
