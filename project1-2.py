#solve for trig roots.

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x=sym.Symbol('x')

#Trigf = cos sin or tan
#A(Trigf(bx-c))+D
class Trig_Functions:
    def Graph_trig(self,Trigf,A,B,C,D):

        print("graph")

    def Trig_Roots(self,A,B,C,D):


        if self.trigf == "sin":
            root = sym.solve(A * float(sym.sin(B * x + C)) + D)
            print("First two roots:".format(root))

        elif self.trigf =="cos":
            root = sym.solve(A * sym.cos(B * x + C) + D)
            print("First two roots:".format(root))

        else:
            root = sym.solve(A * sym.tan(B * x + C) + D)
            print("First two roots:".format(root))



    def GetTrigF(self):

        while True:
            self.trigf = input("sin cos or tan?")

            if self.trigf != ("sin" or "cos" or "tan"):
                print("please input the terms exactly as stated")

            if self.trigf == ("sin" or "cos" or "tan"):
                break





T = Trig_Functions()
T.GetTrigF()
A = float(input(" input the amplitude"))
B = float(input(" input the frequency"))
C = float(input(" input the horizontal shift (radians)"))
D = float(input(" input the vertical shift"))
T.Trig_Roots(A, B,C,D)


