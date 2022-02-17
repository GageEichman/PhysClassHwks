import math
import matplotlib.pyplot as plt
import numpy as np
W= 2
L = W

r = W/2
NP = 1000 #number of points

Points = []
PointsInside = []
PointsOutside = []

# random point variables
X = np.random.uniform(-1,1,NP) #min,max,number of points
Y= np.random.uniform(-1,1,NP)

# x points on axes
x = np.arange(-1,1,.00001)

#generate random points into a list of x and y coords
for i in range(len(X)):
    Points.append((X[i],Y[i]))

for (i,j) in Points:
    dist_to_center = np.sqrt(i**2+j**2)
    if dist_to_center > r:
        PointsOutside.append((i,j))
    elif dist_to_center < r:
        PointsInside.append((i,j))


Area = (L*W) *(len(PointsInside)/len(Points))




xin,yin = zip(*PointsInside)
xout,yout = zip(*PointsOutside)


plt.scatter(X,Y)
plt.scatter(xout,yout,c = "red")
plt.scatter(xin,yin, c = "green")
plt.plot(x,np.sqrt(r-x**2),c = "b")
plt.plot(x,-np.sqrt(r-x**2), c ="b")
plt.suptitle("Monte Carlo Area = {} \n True Area = {}".format(Area, np.pi * r**2))
plt.hlines(y=0,xmin=0,xmax=1,color="purple",label="radius = {}".format(r),linewidth=3)

plt.legend(loc ="upper right",prop={'size': 10})




plt.show()