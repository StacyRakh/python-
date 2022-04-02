# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:18:18 2022

@author: Анастасия Рахманина
"""

# выпадение поля в рулетке (номер 1)
import numpy as np
for i in range (0,10):
    a = input ()
    x = np.random.uniform (0,37)
    if x<=1:
        print ("zero")
    elif 1<x<=19:
        print ("red")
    else:
        print ("black")

# проверка теорем сложения или умножения

import numpy as np
k,m,l = 0,0,0
n = 100
for i in range (0,n):
   
    x = np.random.uniform (0,37)
    if x<=1:
        #print ("zero")
        k = k+1
    elif 1<x<=19:
        # print ("red")
        m = m+1
    else:
        # print ("black")
        l = l+1        
print (k,l,m)
if (k/n)+(l/n)+(m/n)==1:
    print ("теорема сложения вероятностей верна")
else: print ("теорема сложения вероятностей не верна")

# проверка 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
x = np.random.rand(10)
a = sum(x)
num_bins = 5
n,bins,patches = plt.hist(a,num_bins)
plt.xlabel ('a')
plt.ylabel ('Probability of sum')
plt.title ("Histogram")

# задание 3
import numpy as np
import math 
import itertools
k,n = 0,50
a = np.random.randint (0,2,n)
b = np.random.randint (0,2,n)
c = np.random.randint (0,2,n)
d = np.random.randint (0,2,n)
x = a + b +c + d
# print (a,b,c,d)
# print (x)
for i in range (0,n):
    if x [i] == 2:
        k = k+1
        
print (k,n,k/n)
p = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))/2**n
print (p)
            
# задание 4
for p in itertools.product("3465",repeat = 2):
    print (''.join(p))

for p in itertools.permutations("789",3):
    print (''.join(str (i) for i in p))

for p in itertools.combinations('78956', 3):
    print (''.join (p))
