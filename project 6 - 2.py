


import math
import matplotlib.pyplot as plt
import numpy as np

List_of_Points = []
ILIST=[]
JLIST=[]


def RandomPointOG(N):

    for n in range(N):
        j = round(np.random.uniform(-1,1), 2) #y direction
        i = round(np.random.uniform(-1,1), 2) #x direction

        ILIST.append(i)
        JLIST.append(j)

        List_of_Points.append((i,j))
    print("Number of points = ", N)


def RandomPointNormal():
    GaussianD = np.random.Generator.normal(loc = 1, scale = 1, size = None)
    return GaussianD




def Draw_plot_graph(List,xtitle,ytitle):
    for n in List:
        plt.scatter(n[0], n[1], vmin=0, vmax=100)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.show()

def Draw_hist_graph(Int,xtitle,ytitle):
    plt.hist(Int,bins=50)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.show()

GaussD1 = np.random.normal(2,1,10000)
GaussD2 = np.random.normal(2,1,10000)
#np.random.normal(stdev, mean value, # of points)




plt.hist(GaussD1,bins=50)

gs_kw = dict(width_ratios=[1.4, 1], height_ratios=[1, 2])

#fig, axs = plt.subplot_mosaic([['upper right', 'left'],['lower right', 'left']],gridspec_kw=gs_kw, figsize=(5.5, 3.5),constrained_layout=True)
#fig.suptitle('2D Gaussian Distribution', color = "black")
#fig.patch.set_facecolor('xkcd:lavender')


fig = plt.figure(constrained_layout=True)
subfigs = fig.subfigures(1, 2, wspace=0.07, width_ratios=[1.5, 1.])
fig.suptitle('2D Gaussian Distribution', color = "black")
fig.patch.set_facecolor('xkcd:lavender')

axs0 = subfigs[0].subplots(1,1 )
subfigs[0].set_facecolor('xkcd:lavender')
subfigs[0].suptitle('subfigs[0]\nLeft side')
subfigs[0].supxlabel('xlabel for subfigs[0]')



axs1 = subfigs[1].subplots(2, 1)
subfigs[1].set_facecolor('xkcd:lavender')
subfigs[1].suptitle('subfigs[1]')
subfigs[1].supylabel('ylabel for subfigs[1]')
print(axs1[0])
axs1[0].plt.hist(GaussD1,bins=50)
axs1.plt.hist(GaussD2,bins=50)

aaa

plt.show()







#gives avg displacement and a histogram of displacements







'''
def Displacement(List):

    disps_x = []
    disps_y=[]
    for n in List:
        disps_y.append(n[1])
        disps_x.append(n[0])


    Draw_hist_graph(disps_x,"Disp from Origin, x","occurrence")
    Draw_hist_graph(disps_y, "Disp from Origin, y", "occurrence")


    disp_tot = (sum(disps_x),sum(disps_y))
    print("total displacement = ", disp_tot)





#gives length avg and a histogram of lengths
def Length(List):
    lengths = []

    for n in List:
        j = n[1]
        i = n[0]
        length = round(math.sqrt(i * i + j * j), 2)

        lengths.append(length)

    Draw_hist_graph(lengths,"Dist from Origin","occurrence")
    length_avg = sum(lengths) / len(lengths)
    print("Average Length = ",length_avg)




'''

