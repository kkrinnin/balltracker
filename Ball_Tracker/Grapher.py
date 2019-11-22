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
wid = scale * (x_max + pad)
h = scale * (y_max-min(y) + pad)
scale_size = wid - 2 * pad

# create canvas / graph
w = Canvas(master, width=wid, height=h)
w.winfo_toplevel().title("Possition Graph")

# creating the circles for the graph
dots = [(t, w.create_oval(((i+r)*scale),(y_max+2*r)*scale-((j+r)*scale),((i-r)*scale),(y_max+2*r)*scale-((j-r)*scale))) for i,j,t in zip(x,y,t)]

# set up the slider
t_scale = Scale(master, from_=0, to=t_max, length=scale_size, resolution=0.01, orient=HORIZONTAL)
t_scale.set(0)
t_scale.pack()
w.pack()

speed = []
time = []

# calulates the velocity for points next to eachother
for i in range(len(x)-1):
    x_avg_sq = (x[i] - x[i+1]) ** 2
    y_avg_sq = (y[i] - y[i+1]) ** 2
    avg_dis = (x_avg_sq + y_avg_sq) ** 0.5
    avg_time = ((t[i] + t[i+1]) / 2)
    speed = speed + [(avg_dis / avg_time)]
    time = time + [avg_time]

# Set up velocity graph
max_v = max(speed)
h_vel = max_v + 2 * pad
vel_master = Tk()
wid_vel = wid + pad
vel = Canvas(vel_master, width=wid_vel, height=h)
vel.winfo_toplevel().title("Velocity Graph")
# creating the circles for the graph

t_scaler = (wid / (max(time)-min(time)))
offset = min(time) - .01*(max(time)-min(time))
v_scaler = h / max_v
min_v = min(speed) - .5
max_v = max(speed)
vel_dots = [(ii, (vel.create_oval((((ii-offset)*t_scaler)-r),max_v*v_scaler-((jj-min_v)*v_scaler+r),(((ii-offset)*t_scaler)+r),max_v*v_scaler-((jj-min_v)*v_scaler-r)))) for ii,jj in zip(time, speed)]

#vel_dots = [(time, (vel.create_oval(((ii+offset)*t_scaler+r)*scale,(jj+r)*scale,((ii+offset)*t_scaler-r)*scale,(jj-r)*scale))) for ii,jj in zip(time, speed)]
t_scale2 = Scale(vel_master, from_=0, to=t_max, length=scale_size, resolution=0.01, orient=HORIZONTAL)
t_scale2.set(0)
t_scale2.pack()
vel.pack()

# loop to show all icons before a time decided by the slider
def show(display, dots, input_t):
    for t,dot in dots:
        if t < input_t:
            display.itemconfigure(dot, state='normal')
        else:
            display.itemconfigure(dot, state='hidden')

# loop to show all icons before a time decided by the slider
def show_vel(display, vel_dot, input_t):
    for t,dot in vel_dot:
        if t < input_t:
            display.itemconfigure(dot, state='normal')
        else:
            display.itemconfigure(dot, state='hidden')

# update loop
while True:
    w.update_idletasks()
    w.update()
    vel.update_idletasks()
    vel.update()
    show(w, dots, t_scale.get())
    show_vel(vel, vel_dots, t_scale2.get())