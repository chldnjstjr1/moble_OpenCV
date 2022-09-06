# 0210.py
import cv2
import numpy as np
#cap = cv2.VideoCapture(0) # 0번 카메라
cap = cv2.VideoCapture('./data/vtest.avi')
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out1 = cv2.VideoWriter('./data/.mp4',fourcc, 20.0, frame_size)
#out2 = cv2.VideoWriter('./data/record1.mp4',fourcc, 20.0, frame_size,isColor=False)
    
while True:
    retval, frame = cap.read()
    if not retval:
        break   
    out1.write(frame)
    
    img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
    text = 'hello'
    org = (100,100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text, org, font, 1, (255,0,0), 2)
    
   #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #out2.write(gray)        
    cv2.imshow('frame',frame)
    #cv2.imshow('gray',gray)          
    key = cv2.waitKey(25)
    if key == 27:
        break
cap.release()
out1.release()
#out2.release()
cv2.destroyAllWindows()