# -*- coding: utf-8 -*-

from numpy import array, cross
from numpy.linalg import solve, norm
import numpy as np

"""
# Define lines based on points
XA0 = array([2, 9, 2]) 
XA1 = array([1, 1, 1])
XB0 = array([0, 0, 0])
XB1 = array([0, 0, 1])

# compute direction vectors of lines A and B
UA = (XA1 - XA0)
UB = (XB1 - XB0)

find_closest_points(XA0, UA, XB0, UB)
"""

def find_closest_points(P1, V1, P2, V2):
  # Normalize Direction Vectors
  V1 = V1 / norm(V1)
  V2 = V2 / norm(V2)


  # find unit direction vector for line C, which is perpendicular to lines A and B
  # and represents the line segment in between the two lines at the closest point
  V3 = cross(V2, V1)
  V3 /= norm(V3)
  
  # L1 = V1 * t + P1
  # L2 = V2 * s + P2
  # L1 + V3 * r = L2
  # V1 * t + P1 + V3 * r = V2 * s + P2
  # V1 * t - V2 * s + V3 * r = P2 - P1
  # Create matrix of this form
  #    t      s     r
  #[[ vx1 , -vx2 , vx3 | px2-px1 ],
  # [ vy1 , -vy2 , vy3 | py2-py1 ],
  # [ vz1 , -vz2 , vz3 | pz2-pz1 ]]
  # Then solve it to get t s and r.

  # Create Matrix to Solve
  # solve the system derived in user2255770's answer from StackExchange: https://math.stackexchange.com/q/1993990
  # Right hand side of augmented matrix
  RHS = P2 - P1

  # Left hand side of augmented matrix
  LHS = array([V1, -V2, V3]).T

  # Solve for [t, s, r]
  solution = solve(LHS, RHS)
  # print(solution)
  
  # Plug in t and s into original Line Equations
  closest_l1 = P1 + solution[0] * V1
  closest_l2 = P2 + solution[1] * V2

  # Return Points on Each Line
  return (closest_l1, closest_l2)


"""
angle_into_vector(np.pi/4,np.pi/4)

TAKES RADIANS

Uses spherical coordinate calculations to calculate 3d vector position.
Basically finds unit circle vector based on theta_x(theta) and theta_y(phi)
"""
def angle_into_vector(theta_x, theta_y):
  x_vec = np.sin(theta_x) * np.cos(theta_y)
  y_vec = np.sin(theta_y)
  z_vec = np.cos(theta_x) * np.cos(theta_x)
  return array([x_vec, y_vec, z_vec])


"""
TODO!
"""
def camerapixels_into_angles(x,y):
  print(x,y)
