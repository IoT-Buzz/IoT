import cv2
import numpy as np
from graphics import *
from pyfirmata import Arduino, util
import time


def getcamera():
    win = GraphWin("Select Camera", 500, 250)
    win.setBackground(color_rgb(255, 255, 255))
    info = Text(Point(250, 20), "press 0 for laptop camera")
    info1 = Text(Point(250, 80), "press 1 for usb or wifi connected camera")
    info2 = Text(Point(250, 140), "or enter ip address of camera manually")
    info.draw(win)
    info1.draw(win)
    info2.draw(win)

    responseBox = Entry(Point(250, 200), 25)
    responseBox.draw(win)

    win.getMouse()
    response = responseBox.getText()
    win.close()

    if (response == '0' or response == '1'):
        return int(response)
    return response


# http://192.168.66.145:4747/video?640X480

cap = cv2.VideoCapture(getcamera())
cap.set(3, 640)
cap.set(4, 480)

board = Arduino('COM7')

board.digital[9].write(0)
board.digital[11].write(1)
time.sleep(1)
board.digital[9].write(1)
board.digital[11].write(0)
time.sleep(1)
board.digital[9].write(0)
board.digital[11].write(0)


def empty():
    pass


cv2.namedWindow('HSV find led 1')
cv2.resizeWindow('HSV find led 1', 640, 250)
cv2.createTrackbar("hue min", "HSV find led 1", 0, 179, empty)
cv2.createTrackbar("hue max", "HSV find led 1", 179, 179, empty)
cv2.createTrackbar("sat min", "HSV find led 1", 0, 255, empty)
cv2.createTrackbar("sat max", "HSV find led 1", 255, 255, empty)
cv2.createTrackbar("val min", "HSV find led 1", 0, 255, empty)
cv2.createTrackbar("val max", "HSV find led 1", 255, 255, empty)


def findpointer(lower, upper):
    # _, imgp = cap.read()
    # board.digital[11].write(1)
    # imgpb=cv2.GaussianBlur(imgp,(5,5),0)
    # imgHSVp = cv2.cvtColor(imgpb, cv2.COLOR_BGR2HSV)
    # mask=cv2.inRange(imgHSVp,lower,upper)
    # contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # for contour in contours:
    #
    #
    return


i = 0

board.digital[9].write(1)
board.digital[9].write(0)
board.digital[11].write(1)

while True:
    _, img = cap.read()
    imgBlur = cv2.GaussianBlur(img, (5, 5), 0)
    imgHSV = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2HSV)

    hMin1 = cv2.getTrackbarPos("hue min", "HSV find led 1")
    hMax1 = cv2.getTrackbarPos("hue max", "HSV find led 1")
    sMin1 = cv2.getTrackbarPos("sat min", "HSV find led 1")
    sMax1 = cv2.getTrackbarPos("sat max", "HSV find led 1")
    vMin1 = cv2.getTrackbarPos("val min", "HSV find led 1")
    vMax1 = cv2.getTrackbarPos("val max", "HSV find led 1")

    lower1 = np.array([hMin1, sMin1, vMin1])
    upper1 = np.array([hMax1, sMax1, vMax1])
    mask_1 = cv2.inRange(imgHSV, lower1, upper1)

    result = cv2.bitwise_and(img, img, mask=mask_1)

    contours, _ = cv2.findContours(mask_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    findpointer(lower1, upper1)
    candidatec = []
    coc = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= 20 and area <= 220:
            candidatec.append(contour)
            M = cv2.moments(contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            coc.append((cx, cy))
            cv2.circle(img, (cx, cy), 10, (255, 0, 0), 1, cv2.FILLED)
    try:
        cv2.line(img, coc[0], coc[1], (255, 0, 0), 2)
    except:
        print("nothing")



    cv2.drawContours(img, candidatec, -1, (0, 0, 255), 2)
    # print(candidatec)
    # print('\n\n\n\n')
    # print(ncandidatec)

    #
    #
    # try:
    #     area = cv2.contourArea(contours[i])
    #     # print('\n\n\n\n')
    #     if area>=70:
    #         cv2.drawContours(img, contours, i, (0, 0, 255), 2)
    #         print(contours[i])
    #
    #         # print('contour' + str(i))
    #         cv2.putText(img, 'countour ' + str(i), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    #         cv2.putText(img, 'area' + str(area), (20, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    #
    # except:
    #     i=0
    # # cv2.drawContours(img, contours,-1,(0,255,0),2)
    #
    # i=i+1

    cv2.imshow('orignal', img)
    cv2.imshow('HSV',imgHSV)
    cv2.imshow('mask 1', mask_1)

    cv2.imshow('result', result)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
