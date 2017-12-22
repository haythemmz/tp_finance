import random
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math
def normal(x):# la fonction f de l'exercice
    if (x>=0):
        return (2*math.exp(-x**2/2)/math.sqrt(2*math.pi))
    else:
        return 0


def rejet (c):# la méthode de rejet
    y=random.expovariate(1)
    u=random.uniform(0,1)
    while(u>(normal(y)/(c*math.exp(-y)))==True):
        y = random.expovariate(1)
        u = random.uniform(0, 1)
    return y

c=np.linspace(0,10,100)
l=[]
for i in c:
    l.append(normal(i)/rejet(i))# calcul de rapport entre rejet et normal afin de déterminer la constant convenable rapport égal 1
y=np.array(l)
print(c,y)
l=[]
for i in range (0,100):
   l.append(1)
a=np.array(l)
plt.plot(c,y)
plt.plot(c,a)
plt.show()
#min=np.min(y)
#print(min)