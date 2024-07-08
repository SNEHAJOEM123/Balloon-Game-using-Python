import pygame
import random
import cv2 as cv
import numpy as np
import time
score=0

pygame.init()



screen_width,screen_height=1280,720
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Balloon game")
fps=30
clock=pygame.time.Clock()
red,green,blue,white,black=(255,0,0),(0,255,0),(0,0,255),(255,255,255),(0,0,0)

#webcam
# cap=cv.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)

img_balloonred=pygame.image.load("D:/Balloons/redballoon.png").convert_alpha()
img_balloonblue=pygame.image.load("D:/Balloons/redballoon.png").convert_alpha()
img_balloonpink=pygame.image.load("D:/Balloons/redballoon.png").convert_alpha()
rectballoonred=img_balloonred.get_rect()
rectballoonblue=img_balloonblue.get_rect()
rectballoonpink=img_balloonpink.get_rect()
rectballoonred.x,rectballoonred.y=random.randint(50,1200),720
rectballoonblue.x,rectballoonblue.y=random.randint(50,1100),720
rectballoonpink.x,rectballoonpink.y=random.randint(50,1100),720

def reset_blueballoons():
    rectballoonblue.y=720
    rectballoonblue.y-=random.randint(1,5)
    rectballoonblue.x=random.randint(50,1100) 
    

def reset_redballoons():
    rectballoonred.y=720
    rectballoonred.y-=random.randint(1,5)
    rectballoonred.x=random.randint(50,1100) 

def reset_pinkballoons():
    rectballoonpink.y=720
    rectballoonpink.y-=random.randint(1,5)
    rectballoonpink.x=random.randint(50,1100) 



start=True
while start:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            start=False
            pygame.quit()

    #Opencv
    # success,img=cap.read()
    # imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    # imgRGB=np.rot90(imgRGB)
    # frame=pygame.surfarray.make_surface(imgRGB).convert()
    # frame=pygame.transform.flip(frame,True,False)
    # window.blit(frame,(0,0))


    window.fill(white)
    speed=random.randint(0,5)
    rectballoonred.y-=4
    rectballoonblue.y-=4
    rectballoonpink.y-=4
    window.blit(img_balloonred,rectballoonred)
    window.blit(img_balloonblue,rectballoonblue)
    window.blit(img_balloonpink,rectballoonpink)

    if rectballoonred.y<0:
            reset_redballoons()
    elif rectballoonblue.y<0:
            reset_blueballoons()
    elif rectballoonpink.y<0:
        reset_pinkballoons()            



    pygame.display.update()
    clock.tick(fps)
    cv.waitKey(0)        