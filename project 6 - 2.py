import math
import matplotlib.pyplot as plt
import numpy as np


GaussD1 = np.random.normal(0,1,1000)
GaussD2 = np.random.normal(1,2,1000)
#np.random.normal(stdev, mean value, # of points)


fig, axs = plt.subplots(3,1,figsize=(10,10), dpi=100)
fig.suptitle("2D Gaussian Distribution", color = "blue")
fig.patch.set_facecolor('xkcd:lavender')
fig.tight_layout(pad = 3.75)


axs[0].set_title(label = "\u03BC = 1, \u03C3 = 0")
axs[1].set_title(label = "\u03BC = 1, \u03C3 = 2")
axs[2].set_title('2 Dimensional Gaussian Distrbutions')

axs[0].hist(GaussD1, bins = 100, color = "red", label = "projection x",density = True, )
axs[1].hist(GaussD2, bins = 100, color = "green", label = "projection y",density = True)

axs[2].hist2d(GaussD1,GaussD2,density = True, cmap = "Blues",bins = 100 )
sm = plt.cm.ScalarMappable(cmap="Blues", norm=plt.Normalize(vmin=0, vmax=1))
plt.colorbar(sm).set_label("counts in bin")

fig.legend(loc ="upper right",prop={'size': 10})


plt.show()
