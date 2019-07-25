import numpy as np
import cv2


camera = cv2.VideoCapture(0)

while(True):
    ret, frame = camera.read()
    
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


camera.release()
cv2.destroyAllWindows()
