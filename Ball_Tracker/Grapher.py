import numpy as np
import time
import tkinter as tk
from tkinter import *

# loading the csv into an array
textfile = 'test.csv'

# set up graph array and seperate into columns
graph = np.loadtxt(textfile, delimiter=',')
x = graph[:, 0]
y = graph[:, 1]
t = graph[:, 2]

r = 2 # radius
scale = 2 # scalling of graph
master = Tk()

# finding sizes for window
x_max = max(x)
y_max = max(y)
t_max = max(t) + 1
pad = 40
w = scale * (x_max + pad)
h = scale * (y_max + pad)
scale_size = w - 2 * pad

# create canvas / graph
w = Canvas(master, width=w, height=h)
w.pack()

# creating the circles for the graph
dots = [(t, w.create_oval((i+r)*scale,(j+r)*scale,(i-r)*scale,(j-r)*scale)) for i,j,t in zip(x,y,t)]

# set up the slider
t_scale = Scale(master, from_=0, to=t_max, length=scale_size, resolution=0.01, orient=HORIZONTAL)
t_scale.set(0)
t_scale.pack()

# loop to show all icons before a time decided by the slider
def show(display, dots, input_t):
    for t,dot in dots:
        if t < input_t:
            display.itemconfigure(dot, state='normal')
        else:
            display.itemconfigure(dot, state='hidden')

# update loop
while True:
    w.update_idletasks()
    w.update()
    show(w, dots, t_scale.get())