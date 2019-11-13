import numpy as np
import cv2
import tkinter as tk
from tkinter import *
import time

gameActive = True

def quitGame():
    gameActive = False

# Setting sliders
master = Tk()
h1 = Scale(master, from_=0, to=255)
h1.set(11)
h1.pack()
s1 = Scale(master, from_=0, to=255)
s1.set(169)
s1.pack()
l1 = Scale(master, from_=0, to=255)
l1.set(139)
l1.pack()
h2 = Scale(master, from_=0, to=255)
h2.set(56)
h2.pack()
s2 = Scale(master, from_=0, to=255)
s2.set(255)
s2.pack()
l2 = Scale(master, from_=0, to=255)
l2.set(255)
l2.pack()
Button(master, text='Quit', command=(quitGame())).pack()

# setting the start time
start = time.time()

# initalizing the matrix for the ball location over time
ballGraph = []

# capture the camera
cap = cv2.VideoCapture(0)

while(gameActive):
    # Capture frame-by-frame
    ret, camera = cap.read()
    # ret, frame = cap.read()

    # Our operations on the frame come here

    # Display the resulting frame
    cv2.imshow('livefeed',camera)

    # Blurs the image
    blurimage = cv2.blur(camera, (10,10))

    # convert to hsv
    hsv = cv2.cvtColor(blurimage, cv2.COLOR_BGR2HSV)
    # lower_orange = np.array([14,220,110])
    # upper_orange = np.array([18,255,255])
    lower_orange = np.array([h1.get(),s1.get(),l1.get()])
    upper_orange = np.array([h2.get(),s2.get(),l2.get()]) 

    # mask orange
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    cv2.imshow('masked',mask)

    # show orange in camera
    res = cv2.bitwise_and(camera,camera, mask = mask)
    #cv2.imshow('masked color', res)

    # find contours
    ret,thresh = cv2.threshold(res,127,255,0)
    blur = cv2.blur(thresh, (5,5))
    c_img, contours, heirarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)
    if len(contours) > 0:
        ball = max(contours, key=lambda x: cv2.contourArea(x))
        x, y , w, h = cv2.boundingRect(ball)
        camera = cv2.rectangle(camera, (x,y), (x + w, y + h), (0,255, 0), 2)
        ballGraph = ballGraph + [(x + w/2, y + h/2, time.time() - start)]

    # M = cv2.moments(cnt)
    cv2.imshow('countours', camera)

    # updates graph
    master.update_idletasks()
    master.update()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Export the array to a file
out_array = np.array(ballGraph)
np.savetxt('test.csv',  out_array, delimiter=",")