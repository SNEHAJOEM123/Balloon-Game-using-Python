import cv2 as cv
import numpy as np
import time
import pygame
import random
global x_g, y_g
area_g = 3000
count=0
score = 0
x_bal = [0,0,0]
y_bal = [0,0,0]
pygame.init()

def nothing (x):
    pass

cv.namedWindow("Track")
cv.createTrackbar("Lh","Track",0,255,nothing)
cv.createTrackbar("Ls","Track",0,255,nothing)
cv.createTrackbar("Lv","Track",0,255,nothing)

cv.createTrackbar("Uh","Track",255,255,nothing)
cv.createTrackbar("Us","Track",255,255,nothing)
cv.createTrackbar("Uv","Track",255,255,nothing)

capture=cv.VideoCapture(0)
screen_width,screen_height=1920,1080
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Balloon game")
fps=30
clock=pygame.time.Clock()
red,green,blue,white,black=(255,0,0),(0,255,0),(0,0,255),(255,255,255),(0,0,0)

img_balloonred=pygame.image.load("oru.png").convert_alpha()
img_balloonblue=pygame.image.load("oru.png").convert_alpha()
img_balloonblack=pygame.image.load("oru.png").convert_alpha()
rectballoonred=img_balloonred.get_rect()
rectballoonblue=img_balloonblue.get_rect()
rectballoonpink=img_balloonblack.get_rect()
rectballoonred.x,rectballoonred.y=random.randint(50,200),720
rectballoonblue.x,rectballoonblue.y=random.randint(400,650),720
rectballoonpink.x,rectballoonpink.y=random.randint(900,1200),720



#print score in pygMe window
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((100),(200/2))
    window.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def reset_blueballoons():
    rectballoonblue.y=720
    rectballoonblue.x=random.randint(50,200) 
    

def reset_redballoons():
    rectballoonred.y=720
    rectballoonred.x=random.randint(400,650) 

def reset_pinkballoons():
    rectballoonpink.y=720
    rectballoonpink.x=random.randint(900,1200) 



start=True

while True:
    

    # img=cv.imread("cup.jpeg")
    _,act_image = capture.read()
    img = act_image[83:290,110:510]
    cv.imshow("cropped", img)

    img=cv.GaussianBlur(img,(21,21),0)
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    
    l_h=cv.getTrackbarPos("Lh","Track")
    l_s=cv.getTrackbarPos("Ls","Track")
    l_v=cv.getTrackbarPos("Lv","Track")

    u_h=cv.getTrackbarPos("Uh","Track")
    u_s=cv.getTrackbarPos("Us","Track")
    u_v=cv.getTrackbarPos("Uv","Track")

    lb_green= np.array([49,67,134])
    ub_green=np.array([255,255,255])

    mask_g=cv.inRange(hsv,lb_green,ub_green)
    result_g=cv.bitwise_and(img,img,mask=mask_g)
    
    contours_g,heirarcy_g=cv.findContours(mask_g,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) 
    # cv.drawContours(img,contours_g,-1,(233,255,0),2)

    if len(contours_g) != 0:
        # draw in blue the contours that were founded
        # cv.drawContours(img, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours_g, key = cv.contourArea)
        x_g,y_g,w_g,h_g = cv.boundingRect(c)

        # draw the biggest contour (c) in green
        cv.rectangle(img,(x_g,y_g),(x_g+w_g,y_g+h_g),(0,255,0),2)



    # for x in contours_g:
    #     # time.sleep(0.02) 
    #     area_g= cv.contourArea(x)
    #     Moments_g= cv.moments(x)
    #     if(Moments_g["m00"]!=0):
    #         x_g = int(Moments_g["m10"] / Moments_g["m00"])
    #         y_g = int(Moments_g["m01"] / Moments_g["m00"])
    #         # print(x_g,y_g)
    #         cv.circle(img, (x_g, y_g), 5, (255, 255, 255), -1)
    #         # print(type(x_g))        


                


        # cv.imshow("image",img)
    

    cv.imshow("mask_g",mask_g)
    # cv.imshow("hsv",hsv)
    cv.imshow("image_g",img)
    cv.imshow("reuslt_g",result_g)

    lb= np.array([0,0,108])
    ub=np.array([14,255,255])
    
    mask=cv.inRange(hsv,lb,ub)
    result=cv.bitwise_and(img,img,mask=mask)

    if len(contours_g) != 0:
        # draw in blue the contours that were founded
        # cv.drawContours(img, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours_g, key = cv.contourArea)
        area_g = cv.contourArea(c)
        print(area_g)
        x_g,y_g,w_g,h_g = cv.boundingRect(c)

        # draw the biggest contour (c) in green
        cv.rectangle(result,(x_g,y_g),(x_g+w_g,y_g+h_g),(0,255,0),2)
    
    contours,heirarcy=cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) 
    cv.drawContours(img,contours,-1,(233,255,0),2)

    try:
        for i in range(3):
            # time.sleep(0.02) 
            area= cv.contourArea(contours[i])
            Moments= cv.moments(contours[i])
            if(Moments["m00"]!=0):
                x_bal[i] = int(Moments["m10"] / Moments["m00"])
                y_bal[i] = int(Moments["m01"] / Moments["m00"])
                # print(x,y)
                cv.circle(img, (x_bal[i], y_bal[i]), 10, (255, 255, 255), -1)
    except:
        # print("passing")
        pass



        cv.imshow("image",img)
    

    cv.imshow("mask",mask)
    # cv.imshow("hsv",hsv)
    cv.imshow("image",img)
    cv.imshow("reuslt",result)

    if area_g < 1500:
        # print(x_bal,y_bal)
        # inp = input(/)
        for i in range(len(x_bal)):
            if (x_bal[i]-50) < x_g < (x_bal[i]+50) and (y_bal[i]-50) <y_g< (y_bal[i]+50) :
                count+=1
                print (x_bal[i],y_bal[i])
                if 30<x_bal[i]<120 :
                    reset_blueballoons()
                    score+=50
                if 120<x_bal[i]<240:
                    reset_redballoons()
                    score+=50
                if 240<x_bal[i]<360:
                    reset_pinkballoons()  
                    score+=50  
                      

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            start=False
            pygame.quit()

    window.fill(white)
    speed=random.randint(0,5)
    rectballoonred.y-=4
    rectballoonblue.y-=4
    rectballoonpink.y-=4
    window.blit(img_balloonred,rectballoonred)
    window.blit(img_balloonblue,rectballoonblue)
    window.blit(img_balloonblack,rectballoonpink)

    #print score
    font = pygame.font.SysFont(None, 48)
    text=font.render("Score: "+str(score),True,black)
    window.blit(text,(10,10))

    if rectballoonred.y<0:
            reset_redballoons()
    elif rectballoonblue.y<0:
            reset_blueballoons()
    elif rectballoonpink.y<0:
        reset_pinkballoons()            


    final = cv.bitwise_or(result,result_g)

    
    cv.imshow("final",final)
    pygame.display.update()
    clock.tick(fps)

    # print (rectballoonred.x,rectballoonred.y,rectballoonpink.x,rectballoonpink.y,rectballoonblue.x,rectballoonblue.y)
    
    k=cv.waitKey(1)
    if k==27:
        break

cv.destroyAllWindows()