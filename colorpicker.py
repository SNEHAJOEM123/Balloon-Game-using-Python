import cv2 as cv
import numpy as np

def nothing():
    pass
cv.namedWindow('colorpicker')
videocapture=cv.VideoCapture(0)


#create trackbars for color change
cv.createTrackbar('HMin','colorpicker',0,179,nothing)
cv.createTrackbar('SMin','colorpicker',0,255,nothing)
cv.createTrackbar('VMin','colorpicker',0,255,nothing)
cv.createTrackbar('HMax','colorpicker',0,179,nothing)
cv.createTrackbar('SMax','colorpicker',0,255,nothing)
cv.createTrackbar('VMax','colorpicker',0,255,nothing)

#set default values for max hsv trackbars
# cv.setTrackbarPos('Hmax','colorpicker',179)
# cv.setTrackbarPos('Smax','colorpicker',255)
# cv.setTrackbarPos('Vmax','colorpicker',255)
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0
while True:
    ret,frame=videocapture.read()
    blur_frame=cv.GaussianBlur(frame,(5,5),0)
    hsv_frame=cv.cvtColor(blur_frame,cv.COLOR_BGR2HSV)
    hMin = cv.getTrackbarPos('HMin', 'colorpicker')
    sMin = cv.getTrackbarPos('SMin', 'colorpicker')
    vMin = cv.getTrackbarPos('VMin', 'colorpicker')
    hMax = cv.getTrackbarPos('HMax', 'colorpicker')
    sMax = cv.getTrackbarPos('SMax', 'colorpicker')
    vMax = cv.getTrackbarPos('VMax', 'colorpicker')
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    mask = cv.inRange(hsv_frame, lower, upper)
    result = cv.bitwise_and(frame, frame, mask=mask)
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax
    cv.imshow('result', result)
    k=cv.waitKey(1)
    if k==27:
        break
cv.destroyAllWindows()        


