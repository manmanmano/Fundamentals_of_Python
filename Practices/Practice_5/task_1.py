import cv2
img = cv2.imread('Images/beautifulview.jpg')
#crop image
startRow = int(296*.20)
startCol = int(474*.20)
endRow = int(296*.80)
endCol = int(474*.80)
croppedImage = img[startRow:endRow, startCol:endCol]
#rotate image
rotationMatrix = cv2.getRotationMatrix2D((474/2, 296/2), 60, .5)
rotatedImage = cv2.warpAffine(img, rotationMatrix, (474, 296))
#detect edges
edge_img = cv2.Canny(img, 100, 200)
#show results
cv2.imshow('Original Image' , img)
cv2.imshow('Cropped Image', croppedImage)
cv2.imshow('Rotated Image', rotatedImage)
cv2.imshow('Detected Edges', edge_img)
cv2.waitKey(0)
