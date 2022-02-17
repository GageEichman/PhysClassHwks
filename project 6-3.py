import math
import matplotlib.pyplot as plt
import numpy as np
W= 2
L = W
H = W
r = W/2
NP = 1000 #number of points

Points = []
PointsZ = []
PointsInside = []
PointsOutside = []

# random point variables
X = np.random.uniform(-1,1,NP) #min,max,number of points
Y= np.random.uniform(-1,1,NP)
Z = np.random.uniform(-1,1,NP)
# x points on axes
x = np.arange(-1,1,.00001)

#generate random points into a list of x and y coords
for i in range(len(X)):
    Points.append((X[i],Y[i]))


for i in range(len(Z)):
    PointsZ.append((X[i],Y[i],Z[i]))

for (i,j) in Points:
    dist_to_center = np.sqrt(i**2+j**2)
    if dist_to_center > r:
        PointsOutside.append((i,j))
    elif dist_to_center < r:
        PointsInside.append((i,j))

PointsOutsidez = []
PointsInsidez = []
for (i,j,k) in PointsZ:
    dist_to_center = np.sqrt(i**2+j**2+k**2)
    if dist_to_center > r:
        PointsOutsidez.append((i,j,k))
    elif dist_to_center < r:
        PointsInsidez.append((i,j,))


Area = (L*W) *(len(PointsInside)/len(Points))
Volume = (L*W*H)*(len(PointsInsidez)/len(PointsZ))




xin,yin = zip(*PointsInside)
xout,yout = zip(*PointsOutside)


plt.scatter(X,Y)
plt.scatter(xout,yout,c = "red")
plt.scatter(xin,yin, c = "green")
plt.plot(x,np.sqrt(r-x**2),c = "b")
plt.plot(x,-np.sqrt(r-x**2), c ="b")

plt.suptitle("Monte Carlo Area = {} \n True Area = {}".format(Area, np.pi * r**2))
plt.hlines(y=0,xmin=0,xmax=1,color="purple",label="radius = {}".format(r),linewidth=3)
t=plt.text(-1,0.75,"Monte Carlo Volume = {}\n True Volume = {}".format(Volume, np.pi* (4/3) * r**3),size = 10)
t.set_bbox(dict(facecolor='yellow', alpha=1, edgecolor='black'))

plt.legend(loc ="upper right",prop={'size': 10})




plt.show()