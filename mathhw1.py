# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:16:41 2022

@author: Анастасия Рахманина
"""


import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 10, 130)
k1=1
k2=int (input("ВВедите число"))
plt.plot(x, np.cos(k1*x))
plt.plot(x, np.cos(k2*x))