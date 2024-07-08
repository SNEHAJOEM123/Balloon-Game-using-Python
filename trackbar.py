import cv2 as cv
import numpy as np

def nothing(): #it does not do anything but is required for trackbar functioning
    pass
cv.namedWindow('controls')
cv.createTrackbar('r','controls',15,300,nothing)
while True:
    img=np.zeros((512,512,3),np.uint8)#create a black image
    img_centre_x=img.shape[0]//2
    img_centre_y=img.shape[1]//2
    radius=int(cv.getTrackbarPos('r','controls'))
    cv.circle(img,(img_centre_y,img_centre_x),radius,(0,0,255),-1)
    cv.imshow('img',img)
    k=cv.waitKey(1)
    if k==27:
        break
cv.destroyAllWindows()        
