#calculate differential of a function
# then graph the differential and the function in the same space but diff plot

#multiple plots same page:
"https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html"

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

# details for the plot



np.seterr(invalid='ignore')                         #ignore some runtime warnings

# stick the function to integrate here as b =
def GivenFunction(a):
    b = np.divide(np.sin(a),a) - 0.05
    return b

#making x values and y values
x = np.arange(-10.0,10.0,0.1)
y = GivenFunction(x)

nx = len(x)
xval = np.array([],dtype = float)

#differentiate here
for i in np.arange(0,nx-1,1):

    diff = (y[i+1] - y[i] )/(x[i+1] - x[i])     #differentiation formula for each point (gives differential btwn next pt.
    #newx = x[i]+diff
    xval = np.append(xval,diff)                   #adding new x values for F prime

print(xval)
print(len(xval))
yval=GivenFunction(xval)



# stuff for plotting
fig, axs = plt.subplots(2,sharex = True)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[0].set_title('Original Function')
axs[1].plot(x, xval) #xval has 1 less than x so cant plot xval or yval with x
axs[1].set_title('F Prime')
axs[1].set_ylim([-0.25,1])

plt.show()
