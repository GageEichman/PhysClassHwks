import matplotlib as plt
import numpy as np
import os

values = np.zeros((10,4),dtype = float)
# make one large array for all values
# values[i,0] = x value in the ith row
# values[i,1] = 'true' y values in the ith row
# values[i,2] = simulated y values in the ith row
# values[i,3] = st dev  in the ith row
# every row constitutes a set of all values we care about for one point
# i = number of points we care about

xypts = "C:/Users/geich/xypts.txt"
f = open(xypts,"r")


for line in f:
    z = line.split()
    xval = z[0]
    ytrueval = z[1]
    ysimulated = z[2]
    stdev = z[3]
    values[line,0].append(xval)
    values[line,1].append(ytrueval)
    values[line,2].append(ysimulated)
    values[line,3].append(stdev)

print(values)


f.close()