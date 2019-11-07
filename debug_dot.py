# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:02:05 2019

@author: McKara
"""
import numpy as np

A = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
print(A)
print(np.shape(A))
T = np.array([1.,2.,3.])
print(T)
print(np.shape(T))
T = np.dot(A,T)
print(T)
print(np.shape(T))