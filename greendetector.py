import cv2 as cv
import numpy as np

videocapture=cv.VideoCapture(0)

while True:
    ret,frame=videocapture.read()
    blur_frame=cv.GaussianBlur(frame,(5,5),0)
    hsv_frame=cv.cvtColor(blur_frame,cv.COLOR_BGR2HSV)
    lower_green=np.array([50,100,20])
    upper_green=np.array([70,255,255])
    mask=cv.inRange(hsv_frame,lower_green,upper_green)
    res=cv.bitwise_and(frame,frame,mask=mask)
   
    
    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("result",res)
    k=cv.waitKey(1)
    if k==27:
        break
cv.destroyAllWindows()        
