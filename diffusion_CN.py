"""
Created on Thu Nov  7 16:10:30 2019
Crank Nicholson scheme for the diffison equation
Dirichlet boundary conditions
@author: McKara
"""

import numpy as np
import matplotlib.pyplot as plt

#Maillage
a = 0
b = np.pi*9
nx = 200
x = np.linspace(a,b,nx)
dx = x[2] - x[1]

#Pas de temps
dt = 40

c = dt/dx**2

A = np.zeros((nx,nx))
A[0,0] = 1
A[nx-1,nx-1] = 1
#Equations du centre
for i in range(1,nx-1,1):
    A[i,i] = 1 + c
    A[i,i-1] = -0.5*c
    A[i,i+1] = -0.5*c

B = np.zeros((nx,nx))
B[0,0] = 1
B[nx-1,nx-1] = 1
#Equations du centre
for i in range(1,nx-1,1):
    B[i,i] = 1 - c
    B[i,i-1] = 0.5*c
    B[i,i+1] = 0.5*c

C = np.dot(np.linalg.inv(A),B)

#Conditions initiales
T = np.cos(x)

tfin = 1000
t = 0
j = 0
while t<tfin and j<50:
    T = np.dot(C,T)
    plt.plot(x,T)
    t = t + dt
    j = j + 1 
    
plt.show()

