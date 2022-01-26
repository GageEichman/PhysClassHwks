#numerical integration
# integrate the function 3 diff ways
# graph the function showing all 3 ways
#then add the scipy integrate function and do it that way, graph this plot, and add text to graph saying result
"http://myweb.ttu.edu/skunori/phys2305/22S/code/week4/integrationA.php"

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import *


class IntegrationMethods:

    def myfunction(self,x):
        y = 2.0 * x**2 + 3.0 * x + 4.0
        return y


    def rectangular(self,dx, xmin, xmax):
        ysum = 0.0
        xx = np.arange(xmin, xmax, dx)
        for x in xx:
            a = x
            b = x + dx
            c = (a + b) / 2.0

            y = dx * IntegrationMethods.myfunction(self, c)
            ysum = ysum + y
        return ysum


    def trapezoidal(self,dx, xmin, xmax):
        ysum = 0.0
        xx = np.arange(xmin, xmax, dx)
        for x in xx:
            a = x
            b = x + dx
            y = dx * (IntegrationMethods.myfunction(self,a)+IntegrationMethods.myfunction(self,b))/2
            ysum = ysum + y
        return ysum



    def simpsons(self, dx, xmin, xmax):
        ysum = 0.0
        xx = np.arange(xmin, xmax, dx)

        for x in xx:
            a = x
            b = x+dx
            c = (a+b)/2
            y = dx/6 *(IntegrationMethods.myfunction(self, a) + 4 * IntegrationMethods.myfunction(self, c) + IntegrationMethods.myfunction(self, b))
            ysum = ysum + y
        return ysum


dx = 0.01
xmin = -5.0
xmax = 5.0

IM = IntegrationMethods()
# three methods to integrate...
result1 = IM.rectangular(dx, xmin, xmax)
result2 = IM.trapezoidal(dx, xmin, xmax)
result3 = IM.simpsons(dx, xmin, xmax)

print('rectangular ', result1)
print('trapezoidal ', result2)
print('simpsons    ', result3)

#  display the sahpe of function.
z = sym.Symbol('x')
print("Derivative to 2z^2 +3z +4 = {}".format(sym.diff(2*z**2 +3*z+4)))

x = np.arange(xmin, xmax, dx)
y = IM.myfunction(x)
fig = plt.figure(1)
plt.plot(x, y, 'g')
fig.text(0.2, 0.8, 'F(x)=2x^2+3x+4', ha='left', va='center')
fig.text(0.2, 0.7, 'F\'(x)= {}'.format(sym.diff(2*z**2 +3*z+4)), ha='left', va='center')
r1 = 'rectangular: ' + str(result1)
r2 = 'trapezoidal: ' + str(result2)
r3 = 'Simpsons: ' + str(result3)
fig.text(0.3, 0.60, r1, ha='left', va='center')
fig.text(0.3, 0.50, r2, ha='left', va='center')
fig.text(0.3, 0.40, r3, ha='left', va='center')
#fig.savefig("myintegrationA.png")



plt.show()


