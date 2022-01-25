#numerical integration
# integrate the function 3 diff ways
# graph the function showing all 3 ways
#then add the scipy integrate function and do it that way, graph this plot, and add text to graph saying result
"http://myweb.ttu.edu/skunori/phys2305/22S/code/week4/integrationA.php"

import numpy as np
import matplotlib.pyplot as plt


def myfunction(x):
    y = 2.0 * x * x + 3.0 * x + 4.0
    return y


def rectangular(dx, xmin, xmax):
    ysum = 0.0
    xx = np.arange(xmin, xmax, dx)
    for x in xx:
        a = x
        b = x + dx
        c = (a + b) / 2.0
        y = dx * myfunction(c)
        ysum = ysum + y
    return ysum


def trapezoidal(dx, xmin, xmax):
    ysum = 0.0
    return ysum


def simpsons(dx, xmin, xmax):
    ysum = 0.0
    return ysum


dx = 0.01
xmin = -5.0
xmax = 5.0

# three methods to integrate...
result1 = rectangular(dx, xmin, xmax)
result2 = trapezoidal(dx, xmin, xmax)
result3 = simpsons(dx, xmin, xmax)

print('rectangular ', result1)
print('trapezoidal ', result2)
print('simpsons    ', result3)

#  display the sahpe of function.
x = np.arange(xmin, xmax, dx)
y = myfunction(x)
fig = plt.figure(1)
plt.plot(x, y, 'g')
fig.text(0.2, 0.8, 'F(x)=2.0*x*x+3.0*x+4.0', ha='left', va='center')
r1 = 'rectangular: ' + str(result1)
fig.text(0.3, 0.70, r1, ha='left', va='center')
fig.savefig("myintegrationA.png")
plt.show()


