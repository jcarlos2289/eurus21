import numpy as np
import cv2
import sys

cap = cv2.VideoCapture('bilbao.MP4')
if cap is None:
    sys.exit('Fallo al cargar video')

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:
       
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
