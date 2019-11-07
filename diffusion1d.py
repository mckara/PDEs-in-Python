"""
15/10/19
Diffusion 1D forward
"""

import numpy as np
import matplotlib.pyplot as plt

#Maillage
a = 0
b = np.pi
nx = 4
x = np.linspace(a,b,nx)
dx = x[2] - x[1]

"""
dx = (b-a)/nx
x = np.arange(a,b+dx*0.001,dx)
"""
#Pas de temps
dt = 0.45*dx**2

#Operateur Laplacien ++
c = dt/dx**2
A = np.zeros((nx,nx))
# Conditions limites de dirichlet
A[0,0] = 1
A[nx-1,nx-1] = 1
#Equations du centre
for i in range(1,nx-1,1):
    A[i,i] = 1 - 2*c
    A[i,i-1] = c
    A[i,i+1] = c
   
#Conditions initiales
#T = np.cos(x)
#T = -5*x + 10
T = np.array(np.ones((4,1)))*2
print(T)
print(np.shape(T))
print(A)
print(np.shape(A))
B = np.dot(A,T)
print(B)
print(np.shape(B))

#tfin = 10
#t = 0
#j = 0
#while t<tfin and j<10:
#    T = np.dot(A,T)
#    plt.plot(x,T)
#    t = t + dt
#    j = j + 1 
#    print(T)
#    print(np.shape(T))
#plt.show()