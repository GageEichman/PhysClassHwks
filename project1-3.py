#solve for trig roots.
#using newtons method

import numpy as np
import matplotlib.pyplot as plt

def Newtons_Method(f,Df,x0,epsilon,max_iter):

    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        Dfxn = Df(xn)

        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn

        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None

        xn = xn - fxn/Dfxn

    print('Exceeded maximum iterations. No solution found.')
    return None



f = lambda x: np.sin(x)+x-2.0
Df = lambda x: np.cos(x)+1.0

root = Newtons_Method(f,Df,1,0.0001,100)
print(root)

x = np.linspace(-10,10,1000)
y = np.sin(x)+x-2.0
plt.plot(x,y,color='red',label="sin(x)+x-2.0")
plt.axvline(x=root,label= "root 1, x = {}".format(root))

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend()
plt.show()


f1 = lambda x: np.sin(x)/x - 0.05
Df1 = lambda x: np.cos(x)/x - np.sin(x)/(x**2)


root1 = Newtons_Method(f1,Df1,1,0.0000001,100)
print(root1)

x = np.linspace(-10,10,1000)
y = np.sin(x)/x-0.05
plt.plot(x,y,color='red',label="sin(x)/x -0.05")

plt.axvline(x=root1,label= "root 1, x = {}".format(root1))
plt.axvline(x=-root1,label= "root 1, x = {}".format(-root1))
plt.axvline(x=root1+np.pi,label= "root 2, x = {}".format(root1+np.pi))
plt.axvline(x=-(root1+np.pi),label= "root 2, x = {}".format(-(root1+np.pi)))
plt.axvline(x=root1+2*np.pi,label= "root 3, x = {}".format(root1+2*np.pi))
plt.axvline(x=-(root1+2*np.pi),label= "root 3, x = {}".format(-(root1+2*np.pi)))

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend()
plt.show()

