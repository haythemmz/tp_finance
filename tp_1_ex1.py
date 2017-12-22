import random
import matplotlib.pyplot as plt
import numpy as np
import statistics
l=[]
m=[]
a=[]
b=[]

def moyenne (n):# fonction qui returne la moyenne et la variance une liste des valeurs aléatoire uniformenet distribuées entre 0 et 1
    for i in range(0, n):
        l.append(random.uniform(0, 1))# liste des valeur aléatoire uniformes entre 0 et 1
    y = np.array(l)
    m=np.mean(y) # la moyenne
    n=statistics.variance(y)#la variance


    return [m,n] # sortie de la fonction ( la moyenne et variance)

print(moyenne(1000))

for i in range (1,100):#faire 10000 tirage
    p=100*i
    a.append(p)
    n=moyenne(p)[0]#calcul de moyenne
    v=moyenne(p)[1]#calcul de variance
    b.append(n)#remplir une liste b par des moyennes

    print("pour {} simulation la moyenne est {} et la variance est {}".format(i,n,v)) # affichage de la moyenne et la varience pour chaque tirage



x=np.array(a)
y=np.array(b)
plt.plot(x,y) # faire une figure dont l'axe des abssaices est les tirages et l"axe des ordonnée est la moyennne


plt.show()# affichage de la figure
