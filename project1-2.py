#solve for trig roots.

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


x=sym.Symbol('x')

#Trigf = cos sin or tan
#A(Trigf(bx-c))+D

class Trig_Functions:
    def Graph_trig(self,A,B,C,D):
        x = np.linspace(-20, 20, 1000)

        if self.trigf == "sin":
            y = (A * (np.sin(B * x + C)) + D)
            print("1")

        elif self.trigf == "cos":
            y = (A * (np.cos(B * x + C)) + D)

        elif self.trigf == "tan":
            y = (A * (np.tan(B * x + C)) + D)


        print("2")
        plt.plot(x, y, color='red', label="sin")
        print("3")
        Trig_Functions.Trig_Roots(self, A, B, C, D)
        plt.axvline(x=self.root[0], label="root , x = {}".format(self.root[0]))

        plt.legend()
        plt.show()





    def Trig_Roots(self,A,B,C,D):


        if self.trigf == "sin":
            self.root = sym.solve(A * (sym.sin(B * x + C)) + D)
            print("First two roots: {}".format(self.root))

        elif self.trigf =="cos":
            self.root = sym.solve(A * sym.cos(B * x + C) + D)
            print("First two roots: {}".format(self.root))

        else:
            self.root = sym.solve(A * sym.tan(B * x + C) + D)
            print("First two roots: {}".format(self.root))



    def GetTrigF(self):

        self.trigf = input("sin cos or tan?")



        if self.trigf == "sin" or self.trigf == "cos" or self.trigf == "tan":
            print("good, now please input the tirg function in standard form")

        else:
            self.trigf = None
            print("please input the terms exactly as stated")

        return self.trigf




T = Trig_Functions()

while True:

    trigf = T.GetTrigF()

    if trigf == None:
        print("Please run again")

    else:
        A = int(input("A-->"))
        B = int(input("B-->"))
        C = int(input("C-->"))
        D = int(input("D-->"))

        T.Trig_Roots(A, B, C, D)
        T.Graph_trig(A, B, C, D)

        break





