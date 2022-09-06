# 0202.py
import cv2

imageFile = './data/lena.png'
img = cv2.imread(imageFile) 
cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])#
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 5])#QUALITY는 사이즈 줄이는것

#========================================================================
imageFileBmp = './data/Lena2.jpg'
bmp = cv2.imread(imageFileBmp)
img  = cv2.imread(imageFile)  
cv2.imshow('Lena color',img)
cv2.imshow('Lena color bmp',bmp)

cv2.waitKey()
cv2.destroyAllWindows()