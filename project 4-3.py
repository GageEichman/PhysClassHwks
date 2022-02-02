#make ode to function given
#plot og function
#plot 3 graphs using RC values of 1.0,0.1,0.01
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *
import scipy as sci

def DrivingV(a):

    y = np.sin(a) + 0.5 * np.sin(100*a)
    return y

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
        yval[i+1] = yn + Fprime(yn,xn,T)*dx
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

'''
fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
plt.plot(x,y,"red",label = 'Vin')
plt.plot(x,y1,"teal", label = "RC = 1 s")
plt.plot(x,y2,"blue", label = "RC = 0.1 s")
plt.plot(x,y3,"pink", label = "RC = 0.01 s")

fig.legend(loc ="upper right",prop={'size': 8})

plt.show()
'''

#--------------------------------------


#the two numbers in fron make a matrix (4,1) with 4 rows and 1 collumn
# to access an individual plot, indice the matrix position (matrix element 1,1 = axs[0,0])
fig, axs = plt.subplots(4,1,sharex = True,sharey = True,figsize=(10,7), dpi=80)
fig.suptitle('RC Lowpass Filter', color = "blue")
fig.patch.set_facecolor('xkcd:mint green')



axs[0].set_title('Signal W/ Noise')
axs[0].plot(x,y, color = "r", label = "")
#axs[0].legend(loc ="upper left",prop={'size': 8})

axs[1].set_title('Low Pass with RC = 1 s')
axs[1].plot(x,y1, color = "g", label = "")
axs[1].plot(x,np.sin(x), color = "r", label = "")
#axs[1].legend(loc ="upper left",prop={'size': 8})

axs[2].set_title('Low pass with RC = 0.1 s')
axs[2].plot(x,y2, color = "g", label = "")
axs[2].plot(x,np.sin(x), color = "r", label = "")
#axs[2].legend(loc ="upper left",prop={'size': 8})

axs[3].set_title('Low pass with RC = 0.01 s')
axs[3].plot(x,y3, color = "g", label = "RC Filter Output")
axs[3].plot(x,np.sin(x), color = "r", label = "Input Signal")
#axs[3].legend(loc ="upper left",prop={'size': 8})
axs[3].legend(bbox_to_anchor=(0, 5),
                         loc='upper left', borderaxespad=0.)



# making legend for axs3, but move it outside the bounds so that it loks like it applies to all of them

#fig.legend(loc ="upper left",prop={'size': 8})

plt.show()


#---
