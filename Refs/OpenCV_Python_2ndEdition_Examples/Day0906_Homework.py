import cv2
import numpy
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('./data/Lena.png')
img_resize = img.resize((50, 50))
img_resize.save('./data/resizelena.jpg')

cap = cv2.VideoCapture('./data/vtest.avi')
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)


while True:   
    retval, frame = cap.read()
    if not retval:
        break
    
    img1 = cv2.imread('./data/resizelena.jpg')
    alpha = 0.5
    img_c = (img1 * alpha + frame_size * (1-alpha)).astype(numpy.uint8)
    cv2.imshow('frame',img_c)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()