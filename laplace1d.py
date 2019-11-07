
"""
10/08/19
Laplace 1D
"""

import numpy as np
import matplotlib.pyplot as plt

a = -1
b = 1
nx = 100
#dx = (b-a)/nx
x = np.linspace(-np.pi,np.pi,nx)
dx = x[3]-x[2]
k = dx**-2
#x = np.array([range(a,b,dx)])

A = np.zeros((nx,nx))
T = np.zeros((nx,1))
B = np.cos(x)

A[0,0] = 1
A[nx-1,nx-1] = 1

#B[0,0] = 100
#B[nx-1,0] = 20

for i in range(1,nx-1,1):
    A[i,i] = -2*k
    A[i,i-1] = k
    A[i,i+1] = k      
    
T = np.dot(np.linalg.inv(A),B)

plt.plot(x,T)
plt.show()