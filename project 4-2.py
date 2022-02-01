#Using eulers method calculat the output voltage for the square input pulse
#graph og squre pulse
# graph ode solution on top


#Write a python code to solve
#y′(x)=−3.0y(x)+cos(x) for the initial value y(0)=1.0 and reproduce the plot from Wolfram Alpha.
# Use Euler's method for this assignment and skip Runge-Kutta this time.

#calculate differential of a function
# then graph the differential and the function in the same space but diff plot

#multiple plots same page:
"https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html"

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *
import scipy as sci





def DrivingV(a):
    yval = np.zeros(len(a))
    for i in range(len(a)):
        xnR = round(a[i],0)
        print(xnR)
        if xnR % 2 == 0:
            yval[i] = 1
        elif xnR % 2 != 0:
            yval[i] = -1
        else:
            print('something broke in DrivingV')
    return yval



def Eulers(y0,x):
    nx = len(x)
    yval = np.zeros(nx)
    yval[0]=y0
    i = 0
    while i < (nx-1):
        xn = x[i]
        yn = yval[i]
        dx = x[i+1]-x[i]
        yval[i+1] = yn + Fprime(yn,xn)*dx
        i = i +1
    print(yval)
    return(yval)

def Fprime(y,a):
    FP = -3 * y + np.cos(a)
    return FP


y0 =1
dx = .1

#making x values and y values
x = np.arange(-10,10,dx)
y = DrivingV(x)

plt.plot(x,y)
plt.show()