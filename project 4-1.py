#Write a python code to solve
#y′(x)=−3.0y(x)+cos(x) for the initial value y(0)=1.0 and reproduce the plot from Wolfram Alpha.
# Use Euler's method for this assignment and skip Runge-Kutta this time.



#multiple plots same page:
"https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html"

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *
import scipy as sci





# stick the function to integrate here as b =
def Fprime(y,a):
    FP = -3 * y + np.cos(a)
    return FP



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












y0 =1
dx = .01

#making x values and y values
x = np.arange(-10,10,dx)
y = Eulers(y0,x)



# stuff for plottin
plt.axhline(y = 0,color = "black")
plt.plot(x,y, color = "r")


plt.show()