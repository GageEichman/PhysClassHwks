#Make similar plots for Moon or Mars or Jupiter. (just chose one. It is your choise.)
#do the graphs from 5.2 but using the g value of those planets


import numpy as np
import matplotlib.pyplot as plt
import random


# general program goes like so:
# array the inital values in a 1*4 matrix
# make a new matrix with rows = to the number of steps (dt) and 4 collumns, one for x,y,vx,and vy
#


def Fprime(states,t,k,g):
    # take derivative of each 'state' and put it in a new numpy array.

    Fp = [states[2],states[3],-k*states[2],-g+-k*states[3]]
    return Fp



def EulersMethod(StateInit,t,k,g):
    vtemp = np.zeros((len(t),len(StateInit)),dtype=float)
    vtemp[0,:] = StateInit

    i = 0
    while i < (len(t)-2):
        tn = t[i]
        dt = t[i+1]-t[i]
        Fp = Fprime(vtemp[i,:],tn,k,g)
        vtemp[i + 1, 0] = vtemp[i,0] + Fp[0] * dt         #x pos
        vtemp[i + 1, 1] = vtemp[i, 1] + Fp[1] * dt     #y pos
        vtemp[i + 1, 2] = vtemp[i, 2] + Fp[2] * dt     #x vel
        vtemp[i + 1, 3] = vtemp[i, 3] + Fp[3] * dt     #y vel

        i += 1
        if vtemp[i,1]<-10000.0:
            break

    val = vtemp[0:i,:]
    return val




gearth = 9.8
gjupiter = 26.0
gmoon = 1.625
gmars = 3.75
kvals = [0.08,0.04,0.02,0.01,0.005,0.0]
gvals = [gjupiter,gearth,gmars,gmoon]


dt = 0.01
tmax = 10000
t = np.arange(0,tmax,dt)

x0 = 0.0
y0 = 0.0
v0 = 600
Theta = np.pi/3
StateInit = [x0, y0, v0*np.cos(Theta), v0*np.sin(Theta)]

fig, axs = plt.subplots(3,4,figsize=(10,10), dpi=100)
#axs[0,0].ticklabel_format(axis = "both", style = 'sci')
fig.tight_layout(pad = 3.75)
fig.suptitle('EQ\'s of Motion for Different Planets', color = "blue")
fig.patch.set_facecolor('xkcd:mint green')
axs[0,0].set_title('g = Jupiter')
axs[0,1].set_title('g = Earth')
axs[0,2].set_title('g = Mars')
axs[0,3].set_title('g = Moon')

j=0
colors = []
for g in gvals:
    p = 0
    for k in kvals:

        if j == 0 :
            color = (random.random(), random.random(), random.random())
            colors.append(color)
        else:
            color = colors[p]

        TempList=EulersMethod(StateInit,t,k,g)

        y = TempList[:,1]
        x =TempList[:,0]
        if j == 0:
            axs[0,j].plot(x,y,c = color,label = "k = {}".format(k))
        else:
            axs[0, j].plot(x, y, c=color)

        y1 = TempList[:,3]
        x1 = t[:len(y1)]
        axs[1,j].plot(x1, y1, c=color)


        xx = TempList[0::1000,0]
        yy = TempList[0::1000,1]
        vy = TempList[0::1000,2]
        vx = TempList[0::1000 ,3]
        axs[2,j].quiver(xx,yy,vy,vx,color = color)
        p+=1

    j +=1

fig.legend(loc ="lower right",prop={'size': 10})
#plt.ylim([-800,800])
#plt.xlim([0,300])
plt.show()