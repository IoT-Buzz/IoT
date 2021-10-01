import cv2
import numpy as np
import hand_recognitions as hrm
import time
from pynput import mouse, keyboard
from graphics import *
# import speech_recognition


mouse1 = mouse.Controller()

sensitivity =1

def voicetype():
    return              #not defined as of now

def getcamera():
    win = GraphWin("Select Camera",500,250)
    win.setBackground(color_rgb(255,255,255))
    info = Text(Point(250,20),"press 0 for laptop camera")
    info1 = Text(Point(250, 80), "press 1 for usb or wifi connected camera")
    info2 = Text(Point(250, 140), "or enter ip address of camera manually")
    info.draw(win)
    info1.draw(win)
    info2.draw(win)

    responseBox = Entry(Point(250,200),25)
    responseBox.draw(win)

    win.getMouse()
    response = responseBox.getText()
    win.close()

    if(response=='0' or response=='1'):
        return int(response)
    return response


cap = cv2.VideoCapture(getcamera())
cap.set(3,640)
cap.set(4,480)

# #declaring variable for calculating frame rate
# pTime = 0
# cTime = 0


#index finger previous coordinates
ixp = 960
iyp = 540
ixpp = 960
iypp = 540

# #middle finger previous coordinates
# mxp = 960
# myp = 540
# mxpp = 960
# mypp = 540

#counters
#i = 0
#count = 0
countr = 0
ts = 0


#using hand_recognitions.py
detector = hrm.handDetector(maxHands=1)


#getting frames in while loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    #goal is to control mouse pointer with our finger
    #finding hands and overlaping on image
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if(len(lmList) != 0):
        ix, iy = lmList[8][1:]
        mx, my = lmList[12][1:]

        #print(ix,iy,mx,my)
        cv2.rectangle(img,(36,30),(536,310),(0,0,255),2)
        #count=count+1

        fingers = detector.fingersUp()
        #print(fingers)
        #print(lmList)
        #print(ix,'  ',iy)


        if fingers[1]==1 and fingers[2]==0 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0  :
            if (ix in range(10,537,1) )and( iy in range(10,311,1)):
                if(abs(ix-ixp)>2):
                    tixp=ixp
                    ixp=(ix+ixp+ixpp)/3
                    ixpp=tixp
                if(abs(iy-iyp)>2):
                    tiyp=iyp
                    iyp=(iy+iyp+iypp)/3
                    iypp=tiyp
                mox = int((ixp - 36) * 3.84)
                moy = int((iyp - 30) * 3.84)
                mouse1.position = (mox,moy)
            else:
                mox=960
                moy=540
                mouse1.position = (mox, moy)
        elif fingers[1]==1 and fingers[2]==0 and fingers[0]==1 and fingers[3]==0 and fingers[4]==0  :
            mox = int(((ixp - 36) * 3.84) + (ix - ixp) * 1)
            moy = int(((iyp - 30) * 3.84) + (iy - iyp) * 1)
            mouse1.position = (mox, moy)
        elif fingers[1]==1 and fingers[2]==1 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0  :
            length, img, arr = detector.findDistance(8, 12, img,draw=True,r=3)
            #print(length)
            if(length<=18):
                if(time.time()-ts>=0.7):
                    mouse1.click(mouse.Button.left,2)
                    ts = time.time()
            else:
                if (time.time() - ts >= 1):
                    mouse1.click(mouse.Button.left, 1)
                    ts = time.time()
        elif fingers[1]==1 and fingers[2]==1 and fingers[0]==1 and fingers[3]==0 and fingers[4]==0  :
            length, img, arr = detector.findDistance(8, 12, img,draw=True,r=3)
            #print(length)
            if(length<=18):
                if(time.time()-ts>=0.5):
                    mouse1.click(mouse.Button.left,2)
                    ts = time.time()
            else:
                if (time.time() - ts >= 1):
                    mouse1.click(mouse.Button.left, 1)
                    ts = time.time()
        elif fingers[1]==0 and fingers[2]==0 and fingers[0]==0 and fingers[3]==0 and fingers[4]==1 :
            if (time.time() - ts >= 1):
                mouse1.click(mouse.Button.right, 1)
                ts = time.time()
        elif fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0 and fingers[3] == 1 and fingers[4] == 1:
            mouse1.press(mouse.Button.left)
        elif fingers[1] == 0 and fingers[2] == 0 and fingers[0] == 0 and fingers[3] == 0 and fingers[4] == 0:
            mouse1.release(mouse.Button.left)
        elif fingers[1] == 0 and fingers[2] == 0 and fingers[0] == 1 and fingers[3] == 0 and fingers[4] == 0:
            voicetype()
    #calculates frame rate
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    # #prints frame rate on camera feed image
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    #shows camera feed
    cv2.imshow('camera', img)
    cv2.waitKey(1)
