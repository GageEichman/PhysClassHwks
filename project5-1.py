#Assignment 5.1: Download the example code-1 and modify the code to calculate
#the trajectory for k=0.01 and trace the projectile to y=-10000 m. Submit your plot.

# use eq of motion and numpy arrays to stor 2d date about the position of the particle

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *
import scipy as sci

'''
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[1, 4])
'''



def Eulers(y0, x):
    nx = len(x)
    yval = np.zeros(nx)
    yval[0] = y0
    i = 0
    while i < (nx - 1):
        xn = x[i]
        yn = yval[i]
        dx = x[i + 1] - x[i]
        yval[i + 1] = yn + Fprime(yn, xn) * dx
        i = i + 1
    print(yval)
    return (yval)

dx = 0.1
x= np.array(0,10,dx)

def xPos(x0):
    nx = len(x)
    xval = np.zeros(nx)
    xval[0]= x0
    i = 0
    while 1 <()