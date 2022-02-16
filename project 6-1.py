
import math
import matplotlib.pyplot as plt
import numpy as np



Vals = [83, 92, 89, 93, 86, 84, 88, 79, 98, 93]
#bins = np.arange(70,110,5)   auto divides the segments into 5 parts
def Draw_hist_graph(Int,xtitle,ytitle):
    plt.hist(Int,bins=8, range = (70,110))
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.show()


Draw_hist_graph(Vals,"Temperature over Ten Days", "Occurence")




