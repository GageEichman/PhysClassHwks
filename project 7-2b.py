# load data that has been saved from 7-2a
# then analyze that data

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.optimize as opt

import os
N =2

# read data from txt files and reformat BACK to an array so its usable here
# outputs the list of all arrays
def ReadData(N):
    Valsdict = {}
    for i in range(N):
        tempfile =open("C:/Users/geich/Desktop/DataFiles/Data_{}.txt".format(i),"r")
        Valsdict["vals_{}".format(i)] = 0
        array = np.loadtxt("C:/Users/geich/Desktop/DataFiles/Data_{}.txt".format(i)).reshape(10,4)
        Valsdict["vals_{}".format(i)] = array
        tempfile.close()
    Valslist = list(Valsdict.values())
    return Valslist



def myChi2(param,values):
    a=param[0]
    b=param[1]
    x=values[:,0]

    ymeas=values[:,2]
    yerror=values[:,3]
    dy=ymeas-(a+b*x)
    cxx=0.0
    print(dy)
    for i in np.arange(len(dy)):
        # print('i ',i)
        cxx=cxx+(dy[i]*dy[i])/(yerror[i]*yerror[i])
    return cxx


# NOT COMPLETELY DONE YET. I DONT KNOW HOW CHI SQUARED FITTING WORKS, BUT IF I DID I COULD USE IT TO PLOT.