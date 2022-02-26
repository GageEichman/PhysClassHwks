import matplotlib as plt
import matplotlib.pyplot as plt
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

j = 0
for line in f:

    z = line.split()
    xval = float(z[0])
    ytrueval = float(z[1])
    ysimulated = float(z[2])
    stdev = float(z[3])

    values[j,0]=(xval)
    values[j,1]=(ytrueval)
    values[j,2]=(ysimulated)
    values[j,3]=(stdev)

    j += 1
j=0

print(values)

x = values[:,0]
y = values[:,1]

y1 = values[:,2]

fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
fig.suptitle("Theoretical Line Value VS. Simulated Values")
plt.plot(x,y,color = 'r')
plt.scatter(x,y1,color = "blue")
plt.show()

f.close()