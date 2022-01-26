#calculate differential of a function
# then graph the differential and the function in the same space but diff plot

#multiple plots same page:
"https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html"

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *
import scipy as sci

z = sym.Symbol('x')

np.seterr(invalid='ignore')                         #ignore some runtime warnings



# stick the function to integrate here as b =
def GivenFunction(a):
    b = np.divide(np.sin(a),a) - 0.05
    return b

#making x values and y values
x = np.arange(-10.0,10.0,0.1)
y = GivenFunction(x)
nx = len(x)
yval = np.array([],dtype = float)



#differentiate here
for i in np.arange(0,nx-1,1):

    diff = (y[i+1] - y[i] )/(x[i+1] - x[i])     #differentiation formula for each point (gives differential btwn next pt.

    yval = np.append(yval,diff)                   #adding new y values for F prime





xval=np.arange(-10.0,9.9,0.1) # have to make x and y arrays match so need to make new one with 199 elements
                              # only 199 in yval cause the for loop loops from 0 to 199



# stuff for plotting
fig, axs = plt.subplots(2,sharex = True,sharey = True)
fig.suptitle('Numerical Differentiation', color = "blue")
fig.patch.set_facecolor('xkcd:mint green')

axs[0].axhline(y = 0,color = "black")
axs[0].plot(x,y, color = "r")
axs[0].set_title('Original Function')

axs[1].axhline(y = 0,color = "black")
axs[1].plot(xval, yval, color = "g")
axs[1].set_title('Differentiated Function')

print("Derivative to sin(z)/z -0.05 = {}".format(sym.diff(sin(z)/z - 0.05,z)))

plt.show()
