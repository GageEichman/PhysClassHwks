import numpy as np

N = 13

Charge = 25 *np.ones((N,1))/N

q=0
for i in range(len(Charge)):
    Charge[i] = Charge[i] * -1
    q +=1
    if q >= round(N/2):
        break

print(Charge)
print(len(Charge))

m = 0
for i in range(len(Charge)):
    m +=Charge[i]

print(m)
