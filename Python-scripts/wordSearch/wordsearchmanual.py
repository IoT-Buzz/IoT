import string
from re import split
import math
import cv2
import numpy


fac =30
thresh=50

    



def findc(ch):
    word=[]
    for i,a in enumerate(maze):
        for j,b in enumerate(a):
            if b==ch:
                #cv2.rectangle(imgrgb,(a[1],a[2]),(a[3],a[4]),(0,0,255),1)
                word.append([i,j])
    return word



def findwordv2(naam):
    a=findc(naam[0])
    length_naam=len(naam)
    for b in a:
        x,y=b[0],b[1]
        score=1
        # print(b)
        for i in range(0,8):
            # print('i is :'+str(i))
            x,y=b[0],b[1]
            for j in range(1,length_naam):
                if(i==0):
                    x,y=x-1,y-1
                elif(i==1):
                    x,y=x-1,y
                elif(i==2):
                    x,y=x-1,y+1
                elif(i==3):
                    x,y=x,y-1
                elif(i==4):
                    x,y=x,y+1
                elif(i==5):
                    x,y=x+1,y-1
                elif(i==6):
                    x,y=x+1,y
                elif(i==7):
                    x,y=x+1,y+1
                # print(j)
                # print(x,y)
                
                #print(naam[j])
                if x>=0 and x<len_column and y>=0 and y<len_row:
                    if(maze[x][y]==naam[j]):
                        score=score+1
                # print(score)
            # print('score is '+ str(score))
            if(score>=length_naam):
                print("starting index is :",end=' ')
                print(b)
                print("i is :",end=' ')
                print(i)
                y1,x1=b[0]*fac+(thresh/2),b[1]*fac+(thresh/2)
                if i==0:
                    x2,y2=(b[0]+1-len(naam))*fac+(thresh/2),(b[1]+1-len(naam))*fac+(thresh/2)
                elif i==1:
                    x2,y2=(b[0]+1-len(naam))*fac+(thresh/2),(b[1])*fac+(thresh/2)
                elif i==2:
                    x2,y2=(b[0]+1-len(naam))*fac+(thresh/2),(b[1]+len(naam)-1)*fac+(thresh/2)
                elif i==3:
                    x2,y2=(b[0])*fac+(thresh/2),(b[1]-len(naam)+1)*fac+(thresh/2)
                elif i==4:
                    x2,y2=(b[0])*fac+(thresh/2),(b[1]+len(naam)-1)*fac+(thresh/2)
                elif i==5:
                    x2,y2=(b[0]-1+len(naam))*fac+(thresh/2),(b[1]-len(naam)+1)*fac+(thresh/2)
                elif i==6:
                    x2,y2=(b[0]-1+len(naam))*fac+(thresh/2),(b[1])*fac+(thresh/2)
                elif i==7:
                    x2,y2=(b[0]-1+len(naam))*fac+(thresh/2),(b[1]+len(naam)-1)*fac+(thresh/2)
                
                cv2.line(img,(int(x1),int(y1)),(int(y2),int(x2)),(0,255,0),2)
                break
            else:
                score=1



def showMaze():
    for i,a in enumerate(maze):
        for j,b in enumerate(a):
            cv2.putText(img,b,(j*fac+int((thresh/2)),i*fac+int((thresh/2))),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
    cv2.imshow('test',img)
    cv2.waitKey(0)





maze=[[]]

len_row= int(input("enter no. of columns: "))
len_column= int(input("enter no. of rows: "))

for i in range(0,len_column):
    row=input('enter '+str(i)+'th row: ')
    maze[i]=row.split()
    if(i<len_column-1):
        maze.append([])

# print('enter maze data properly')
# maze_data = input()

sz=(len_column*fac+thresh,len_row*fac+thresh)
img=numpy.zeros(sz)
img[:] = 1



for i in range(0, len_column):
    print(maze[i])

names= input('enter words you want to find')
names=names.split(' ')
for nam in names:
    nam=nam.upper()
    print(nam)
    findwordv2(nam)

showMaze()

