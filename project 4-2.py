#Using eulers method calculat the output voltage for the square input pulse
#graph og squre pulse
# graph ode solution on top



#multiple plots same page:
"https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html"

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *
import scipy as sci





def DrivingV(a):
    #print(a)
    a = x
        #changed as to x's, change them back
    yval = np.zeros(len(a))
    for i in range(len(a)):
        xnR = round(a[i],0)
        #print(xnR)
        if xnR % 2 == 0:
            yval[i] = 1
        elif xnR % 2 != 0:
            yval[i] = -1
        else:
            print('something broke in DrivingV')
    return yval

def Fprime(y,a,T):
    FP = 1/T * (DrivingV(a)-y)
    return FP

def Eulers(y0,x,T):
    nx = len(x)
    #print(x)
    yval = np.zeros(nx)
    yval[0]=y0
    i = 0
    while i < (nx-1):
        xn = x[i]
        yn = yval[i]
        dx = x[i+1]-x[i]
        #print(Fprime(yn,xn,T))
        yval[i+1] = yn + Fprime(yn,xn,T)[i]*dx
        i = i +1
    #print(yval)
    return(yval)



y0 = 0
dx = .01

T1 = 1
T2 = 0.1
T3 = 0.01

#making x values and y values
x = np.arange(0,10,dx)
y = DrivingV(x)
y1 = Eulers(y0,x,T1)
y2 = Eulers(y0,x,T2)
y3 = Eulers(y0,x,T3)

fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
plt.plot(x,y,"red",label = 'Vin')
plt.plot(x,y1,"teal", label = "RC = 1 s")
plt.plot(x,y2,"blue", label = "RC = 0.1 s")
plt.plot(x,y3,"pink", label = "RC = 0.01 s")

fig.legend(loc ="upper right",prop={'size': 8})

plt.show()