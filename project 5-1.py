import numpy as np
import matplotlib.pyplot as plt


# general program goes like so:
# array the inital values in a 1*4 matrix
# make a new matrix with rows = to the number of steps (dt) and 4 collumns, one for x,y,vx,and vy
#


def Fprime(states,t,k,g):
    # take derivative of each 'state' and put it in a new numpy array.

    Fp = [states[2],states[3],-k*states[2],-g-k*states[3]]
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
        if vtemp[i,1]<-1000.0:
            break

    val = vtemp[0:i,:]
    return val


dt = 0.01
tmax = 100
t = np.arange(0,tmax,dt)

x0 = 0.0
y0 = 0.0
v0 = 600
Theta = np.pi/3
g = 9.8
k=0.1

StateInit = [x0, y0, v0*np.cos(Theta), v0*np.sin(Theta)]

Eqs = (EulersMethod(StateInit,t,k,g))
Eqs1 = (EulersMethod(StateInit,t,0,g))


x = Eqs[:,0]
y = Eqs[:,1]

fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
plt.plot(x,y,"red",label = 'k =0.1' )
#plt.plot(Eqs1[:,0],Eqs1[:,1],"blue",label = 'k =0')
fig.suptitle("ball shot upwards agianst air resistance and gravity")
fig.legend(loc ="upper right",prop={'size': 8})

plt.show()

