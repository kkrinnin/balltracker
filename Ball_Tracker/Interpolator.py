import numpy as np
import time
import tkinter as tk
from tkinter import *
import math

# loading the csv into an array
camera1 = 'camera1.csv'
camera2 = 'camera2.csv'
# import as x1, y1, t1, x2, y2, t1
graph1 = np.loadtxt(camera1, delimiter=',')
graph2 = np.loadtxt(camera2, delimiter=',')

x1 = graph1[:, 0]
y1 = graph1[:, 1]
t1 = graph1[:, 2]
x2 = graph2[:, 0]
y2 = graph2[:, 1]
t2 = graph2[:, 2]

# set camera settings
camera1_x_fov = 120
camera2_x_fov = 120
camera1_x_res = 100
camera1_y_res = 50
camera2_x_res = 100
camera2_y_res = 50
camera1_y_fov = camera1_y_res / camera1_x_res * camera1_x_fov
camera2_y_fov = camera2_y_res / camera2_x_res * camera2_x_fov

# find the pixel angle from the center normal

# phi = tan^-1( (2 * distance from center * tan(fov)) / (camera pixel width) )
x_phi1 = np.arctan((2 * x1 * math.tan(camera1_x_fov)) / (camera1_x_res))
x_phi2 = np.arctan((2 * x2 * math.tan(camera2_x_fov)) / (camera2_x_res))
y_phi1 = np.arctan((2 * y1 * math.tan(camera1_y_fov)) / (camera1_y_res))
y_phi2 = np.arctan((2 * y2 * math.tan(camera2_y_fov)) / (camera2_y_res))