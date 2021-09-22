from os import path
import cv2
import numpy as np
import math
import random
import time
from playsound import playsound
from threading import Thread
from pathlib import Path
import winsound
from graphics import *



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



def play_sound_score():
    winsound.PlaySound('sounds//score.wav', winsound.SND_FILENAME)


def play_sound_coll():
    winsound.PlaySound('sounds\collision.wav', winsound.SND_FILENAME)

speed=5

px,py,pw,ph=0,0,0,0

si=1

def gameover():
    winsound.PlaySound('sounds\game_over.wav', winsound.SND_FILENAME)

heart = cv2.imread("face\\heart.png",-1)
heart=cv2.cvtColor(heart,cv2.COLOR_BGRA2RGBA)
alpha_mask_heart = heart[:, :, 3] / 255.0
img_overlay_heart = heart[:, :, :3]


def showLives(l,img):
    x=10

    for iter_2 in range(l):
        overlay_image_alpha(img,img_overlay_heart,x,10,alpha_mask_heart)
        x+=60

def showScore(s,img):
    cv2.putText(img,"score : "+str(s),(450,20),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

def overlay_image_alpha(img, img_overlay, x, y, alpha_mask):
    """Overlay `img_overlay` onto `img` at (x, y) and blend using `alpha_mask`.

    `alpha_mask` must have same HxW as `img_overlay` and values in range [0, 1].
    """
    # Image ranges
    img_overlay=cv2.cvtColor(img_overlay, cv2.COLOR_RGB2BGR)
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to do
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    # Blend overlay within the determined ranges
    img_crop = img[y1:y2, x1:x2]
    img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
    alpha = alpha_mask[y1o:y2o, x1o:x2o, np.newaxis]
    alpha_inv = 1.0 - alpha

    img_crop[:] = alpha * img_overlay_crop + alpha_inv * img_crop


def checkCollision(face,p1,p2,fn):
    top=0
    bottom=480
    top1=0
    bottom1=480
    if p1 ==0:
        top=52
        bottom=235
    elif p1 ==1:
        top=111
        bottom=274
    elif p1 ==2:
        top=146
        bottom=310
    elif p1 ==3:
        top=180
        bottom=355
    elif p1 ==4:
        top=228
        bottom=388
    if p2 ==0:
        top1=52
        bottom1=235
    elif p2 ==1:
        top1=111
        bottom1=274
    elif p2 ==2:
        top1=146
        bottom1=310
    elif p2 ==3:
        top1=180
        bottom1=355
    elif p2 ==4:
        top1=228
        bottom1=388
    if(face[0]+face[2]/2<130-fn and face[0]+face[2]/2>30-fn):
        if face[1]<top or face[1]+face[3]>bottom:
            return 1
    if(face[0]+face[2]/2>243-fn and face[0]+face[2]/2<343-fn):
        if face[1]<top1 or face[1]+face[3]>bottom1:
            return 1
    return 0
    

cap = cv2.VideoCapture(getcamera())
#cv2.data.haarcascades +
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pipes=[cv2.imread("pipes\\pipe1.png",-1),cv2.imread("pipes\\pipe2.png",-1),cv2.imread("pipes\\pipe3.png",-1),cv2.imread("pipes\\pipe4.png",-1),cv2.imread("pipes\\pipe5.png",-1)]
# for pipe in pipes:
#     # pipe=cv2.cvtColor(pipe,cv2.COLOR_BGRA2RGBA)
#     cv2.imshow("pipes",pipe)
#     cv2.waitKey(0)
# crown=cv2.cvtColor(crown,cv2.COLOR_RGBA2BGRA)
# print(crown.shape)

f_png = cv2.imread("face\\face.png",-1)
# f_png=cv2.cvtColor(f_png,cv2.COLOR_BGRA2RGBA)
alpha_mask_face = f_png[:, :, 3] / 255.0
img_overlay_face = f_png[:, :, :3]
        
n_con_col=8
col_chk=[]
for i in range(n_con_col):
    col_chk.append(0)


frameno=1

score=0
lives=3

f_png = cv2.imread("face\\face.png",-1)

# print(crown[:,:,3])
# cv2.imshow("crown",crown)
# cv2.waitKey(0)
i=0
f=[random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4)]

# t_start = time.time()
# gameover()
# print(t_start)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    # print(frame.shape)
    if not ret:
        break
    
    frameno+=1
    # if(i>600):
    #     i=0
    i+=speed
        # i=i%5
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    

    height, width = gray.shape
    
    if i>213 :
        f[0]=f[1]
        f[1]=f[2]
        f[2]=f[3]
        f[3]=random.randint(0,4)
        score+=1
        thread = Thread(target=play_sound_score)
        thread.start()
        i=0

    img_result = frame[:, :, :3].copy()
    j=0
    while j<4:
        alpha_mask = pipes[f[j]][:, :, 3] /255
        # print(pipes[1][50,20,3])
        img_overlay = pipes[f[j]][:, :, :3]
        overlay_image_alpha(img_result, img_overlay, (213*j)-round(i), 0, alpha_mask)
        j+=1
    
    cv2.line(img_result,(250,0),(250,480),(0,0,255),2)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    # print(faces)

    if(len(faces)>0):
        _x,_y,_w,_h=faces[0]
        # cv2.rectangle(img_result, (_x, _y), (_x+_w, _y+_h), (255, 0, 0), 2)
        f_png_r=cv2.resize(f_png,(_w,_h))
        alpha_mask_face = f_png_r[:, :, 3] / 255.0
        img_overlay_face = f_png_r[:, :, :3]
        if(frameno>100):
            overlay_image_alpha(img_result, img_overlay_face,_x,_y,alpha_mask_face)
            fc=[_x,_y,_w,_h]
            for b in range(n_con_col-1):
                col_chk[b]=col_chk[b+1]
            col_chk[n_con_col-1]=checkCollision(fc,f[0],f[1],i)
            px,py,pw,ph=_x, _y, _w, _h

        flag=1
        for iter in range(n_con_col-1,0+round(speed/7),-1):
            if(col_chk[iter]==0):
                flag=0
        if(flag==1):
            # print(col_chk)
            if(lives>1):
                thread1 = Thread(target=play_sound_coll)
                thread1.start()
            for ye_variable_khi_aur_use_nhi_hua_1 in range(n_con_col-1):
                col_chk[ye_variable_khi_aur_use_nhi_hua_1]=0
            lives-=1

    
    showLives(lives,img_result)
    showScore(score,img_result)


    if score>7*si and speed<20:
        speed+=1
        si+=1

    # print(speed)

    if(lives==0):
        gameover()
        break

    if len(faces)==0 and frameno>100 :
        _x, _y, _w, _h=px,py,pw,ph
        # cv2.rectangle(img_result, (_x, _y), (_x+_w, _y+_h), (255, 0, 0), 2)
        if(_w>10 and _h>10):
            f_png_r=cv2.resize(f_png,(_w,_h))
            alpha_mask_face = f_png_r[:, :, 3] / 255.0
            img_overlay_face = f_png_r[:, :, :3]
            overlay_image_alpha(img_result, img_overlay_face,_x,_y,alpha_mask_face)
        
            
        
        fc=[_x,_y,_w,_h]
        # print(_w)
    cv2.putText(img_result,"made by rahul guglani",(10,450),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
    img_result=cv2.resize(img_result,(round(640*1.8),round(480*1.8)))
    cv2.imshow("camera",img_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
