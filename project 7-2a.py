# simulate N number of experiments from 7.1

import matplotlib.pyplot as plt
import numpy as np
import os

# i had to make this function because python  cant store constants
# my code was rewriting the entire values array, so this fixes the problem by making a new values array everytime a new values array needs to be made
# this allows the program to "store" the values array, albeit in a ghetto manner
def Store_constant_values():
    # make one large array for all values
    values = np.zeros((10, 4), dtype=float)
    # values[i,0] = x value in the ith row
    # values[i,1] = 'true' y values in the ith row
    # values[i,2] = simulated y values in the ith row
    # values[i,3] = st dev  in the ith row
    # every row constitutes a set of all values we care about for one point
    # i = position number of points we care about

    # generate the true x and y values (same for every experiment so leave out of function)
    Truexvals = np.arange(0, 10, 1)
    Trueyvals = []
    stdev = 0.1
    for x in Truexvals:
        y = 2.0 + 3 * x
        Trueyvals.append(y)

    # then append x,y true vals and stdev to total values array
    for i in range(len(Truexvals)):
        values[i, 0] = Truexvals[i]
        values[i, 1] = Trueyvals[i]
        values[i, 3] = stdev
    return values, Truexvals, Trueyvals, stdev

# define original values list so simulateY has variables to mess with


#simulate new y values for each experiment
def SimulateY():
    SimyVals = []

    for j in range(len(Truexvals)):
        Simy = float(Trueyvals[j]+np.random.normal(0.0,stdev,1))
        SimyVals.append(Simy)
    return SimyVals



# generate new values arrays (including all info + simulated stuff) and add them to a dictionary that contains ALL values
def GenNewVals(N):
    Valsdict = {}

    # for every experiment you want to do...
    for j in range(N):
        #re-call the function because you want to generate a new values list to change (so your'e not changing the OG values array)
        values, Truexvals, Trueyvals, stdev = Store_constant_values()
        Valsdict["vals_{}".format(j)] = values
        SimYvals = SimulateY()


        # ... generate a new set of simulated y's, and add them to the parameter array...
        #... then add them to the list that contains ALL values
        for i in range(len(Truexvals)):
            Valsdict["vals_{}".format(j)][i, 2] = float(SimYvals[i])

    return Valsdict



def WriteValsToFile(N):

    TempVals = GenNewVals(N)

    for i in range(N):
        TempData = TempVals["vals_{}".format(i)]
        tempfile = open("C:/Users/geich/Desktop/DataFiles/Data_{}.txt".format(i),"w+")
        print(TempData)

        for row in TempData:
            
            np.savetxt(tempfile,row)

        tempfile.close()



values, Truexvals, Trueyvals, stdev = Store_constant_values()
N = 2

WriteValsToFile(2)








'''
#deletes files in the folder
for m in range(N):
    os.remove("C:/Users/geich/Desktop/DataFiles/Data_{}.txt".format(m))
'''



'''
# old code for JUST plotting points
plt.figure()

for k in range(N):
    x = GenNewVals(N)["vals_{}".format(k)][:, 0]
    y = GenNewVals(N)["vals_{}".format(k)][:, 2]
    plt.scatter(x,y)
plt.plot(Truexvals,Trueyvals)
plt.show()
'''
