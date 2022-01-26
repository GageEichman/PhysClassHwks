# plot a bunch of gaussian curves
#then integrate them to get cum distribution
# tehn plot them


"http://myweb.ttu.edu/skunori/phys2305/22S/week3StepByStep.php"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy.integrate as integrate

def myfunction(x,param):
   # coefficients are transferred through param.
   mu=param[0]
   sig2=param[1]
   a=1.0/np.sqrt(2.0*sig2*np.pi)
   b=(x-mu)*(x-mu)/(2.0*sig2)
   y=a*np.exp(-b)

   return y


def rectangular(xx,param):
   ysum = 0.0
   ycumulative=np.zeros(len(xx))
   i = 0
   dx =xx[1]-xx[0]
   for x in xx:
      a = x
      b = x + dx
      c = (a + b) / 2.0

      y = dx * myfunction(c,param)
      ysum = ysum + y
      ycumulative[i]=ysum
      i = i + 1
   return ysum, ycumulative

x=np.arange(-5.0,5.0,0.01)

mu1=0.0
sig1=0.2
param1=np.array([mu1,sig1])
y1=myfunction(x,param1)
yintegrated1,ycumulative1 = rectangular(x,param1)

mu2=0.1
sig2=0.8
param2=np.array([mu2,sig2])
y2=myfunction(x,param2)
yintegrated2,ycumulative2 = rectangular(x,param2)

mu3=2
sig3=.7
param3=np.array([mu3,sig3])
y3=myfunction(x,param3)
yintegrated3,ycumulative3 = rectangular(x,param3)

mu4=-2.5
sig4=0.9
param4=np.array([mu4,sig4])
y4=myfunction(x,param4)
yintegrated4,ycumulative4 = rectangular(x,param4)

fig, axs = plt.subplots(1,2,sharex = True,sharey = True)
fig.suptitle('Numerical Integration', color = "blue")
fig.patch.set_facecolor('xkcd:mint green')

axs[0].set_title('Original Functions')
axs[0].axhline(y = 0,color = "black")

axs[0].plot(x,y1, color = "r")
axs[0].plot(x,y2, color = "g")
axs[0].plot(x,y3, color = "purple")
axs[0].plot(x,y4, color = "blue")


axs[1].set_title('Integrated Functions')
axs[1].axhline(y = 0,color = "black")
axs[1].plot(x, ycumulative1, color = "r")
axs[1].plot(x, ycumulative2, color = "g")
axs[1].plot(x, ycumulative3, color = "purple")
axs[1].plot(x, ycumulative4, color = "blue")



plt.show()


