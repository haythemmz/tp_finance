import random
import matplotlib.pyplot as plt
import numpy as np



l=[]
g=[]
moyenne=[]
for i in range (0,1000):
    a=random.uniform(0,1)
    l.append(a)
    x=np.array(l)
    moyenne.append(np.var(x))
    g.append(i)


abssaice=np.array(g)
ordonne=np.array(moyenne)
plt.plot(abssaice,ordonne)
plt.show()