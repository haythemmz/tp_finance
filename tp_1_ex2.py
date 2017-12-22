import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import  stats

def expo(lamda,y): # fonctione inverse
    x = -(1/lamda) * math.log(y)
    return x

l=[]
a=[]
for i in range (0,1000):# 1000 tirage
    a.append(i)
    y = random.uniform(0, 1)# loi uniforme
    l.append(expo(2,y))#loi expo
#plt.plot(np.array(a), np.array(l))# courbe la simulation en fonction du rang de tirage



z=0


p=[]
e=[]
y=[]
m=20

for j in range(1,3):
    for i in range (0,1000):
        p.append(i*m/1000)
        y.append(0.5*j*math.exp(-0.5*j*p[i]))
    plt.plot(np.array(p), np.array(y))

plt.show()
