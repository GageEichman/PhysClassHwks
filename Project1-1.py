# quadratic equation roots solver,
# check that Jupyter is working,
# solve for trig roots.

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


x=sym.Symbol('x')

class Quad_Functions:

    def Quad_roots(self,a,b,c):
        if (b*b)-4*a*c <0:
            print("discriminant < 0, roots are complex")
            self.root1 = (-b + np.sqrt((b * b) - 4 * a * c + 0j)) / (2 * a)
            self.root2 = (-b - np.sqrt((b * b) - 4 * a * c+ 0j)) / (2 * a)
            print("roots, x =", self.root1, self.root2)
            return self.root1, self.root2
        else:
            print("discriminant > 0, roots are real")
            self.root1 = (-b + np.sqrt((b*b)-4*a*c))/(2*a)
            self.root2 = (-b - np.sqrt((b*b)-4*a*c))/(2*a)
            print("roots, x = ", self.root1,self.root2)
            return self.root1, self.root2

    def Quad_Max_Min(self,a,b,c):
        der= sym.diff(a*x**2+b*x+c)
        max_min = sym.solve(der)
        max_min_coords = (max_min[0],a*(max_min[0])**2+b*(max_min[0])+c)

        if max_min[0] < 0:
            print("there is a minimum(vertex) at (x,y) =",max_min_coords)

        else:
            print("there is a maximum(vertex) at (x,y) =",max_min_coords)

    def Plot_Quad(self,a,b,c):
        x = np.linspace(-20,20,1000)
        y = a*x**2 + b*x +c
        plt.plot(x,y,color='red',label="{}X^2 + {}X + {}".format(a,b,c))


        if (b*b)-4*a*c < 0 :
            print("discriminant negative, no graphable roots")
        else:
            Quad_Functions.Quad_roots(self, a, b, c)
            plt.axvline(x=self.root1,label= "root 1, x = {}".format(self.root1))
            plt.axvline(x=self.root2,label = "root 2, x = {}".format(self.root2))
        plt.legend()
        plt.show()




Q = Quad_Functions()
print("input the Quadratic coefficients")
A = float(input("a -->"))
B = float(input("b -->"))
C = float(input("c -->"))

Q.Quad_roots(A,B,C)
Q.Quad_Max_Min(A,B,C)
Q.Plot_Quad(A,B,C)