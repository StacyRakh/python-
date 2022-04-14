# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:06:58 2022

@author: Анастасия Рахманина
"""
# Задание 6.1
import numpy as np
import matplotlib.pyplot as plt 
A = np.array ([[1,2,3], [4,0,6], [7,8,9]])
B = np.array ([12,2,1])
print (np.linalg.solve (A,B))

# 6.2
import numpy as np
import matplotlib.pyplot as plt 
A = np.array ([[1,2,-1], [3,-4,0], [8,-5,2], [2,0,-5],[11,4,-7]])
B = np.array ([1,7,12,7,15])
print(np.linalg.solve (A,B))
 
# 6.3 
import numpy as np
import matplotlib.pyplot as plt 
A = np.array ([[1,2,3], [4,5,6], [7,8,9]])
B = np.array ([12,2,1])
dim = np.concatenate ((A,B.T), axis = 1)
print (dim)
np.linalg.matrix_rank(A,0.0001), np.linalg.matrix_rank(dim,0.0001)
A = np.array ([[1,2,3], [4,0,6], [7,8,9]])
B = np.array ([12,2,1])
np.linalg.solve (A,B)

# 6.4
import numpy as np
import matplotlib.pyplot as plt 
import scipy
import scipy.linalg
A = np.array ([[1,2,3], [2,16,21], [4,28,73]])
P,L,U = scipy.linalg.lu (A)
print (P)
print (L)
print (U)

# 6.5
import numpy as np
import matplotlib.pyplot as plt 
def Q(x,y,z):
 return (x**2+y**2+z**2)
x = np.linspace (-1,5,200)
y = np.linspace (-1,5,200)
z = np.linspace (-1,5,200)
plt.plot (x, Q(x, 0.5+ 0.5*z-0.5*x, 6-4*x+2.5*y))
plt.xlabel ('x')
plt.ylabel ('y')
plt.zlabel ('z')
plt.grid (True)
plt.show ()
A = np.array ([[1,2,-1], [8,-5,2]])
B = np.array ([1,12])
np.linalg.lstsq (A,B)
x = np.linspace (-1,5,200)
plt.plot (x, Q(x, 0.5+0.5*z-0.5*x, 6-4*x+2.5*y))
plt.xlabel ('x')
plt.ylabel ('y')
plt.zlabel ('z')
plt.grid (True)
plt.show ()


# 6.6
import numpy as np
A = np.array ([[1,2,3], [4,5,6], [7,8,9]])
B = np.array ([2, 5,11])
Q, R = np.linalg.qr(A)
print (A)
print (Q)
print (R)
R1 = R[:2, :2]
R1
B1 = np.dot (np.transpose (Q), B)[:2]
B1
X1 = np.linalg.solve (R1,B1)
X1
X = np.append (X1,0)
print (X)
np.linalg.norm (X)

np.linalg.norm (np.dot (A,X)- B)
X = np.array  ([1.5, 1, 0.5])
np.linalg.norm (X), np.linalg.norm (np.dot (A,X)- B)

