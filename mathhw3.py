# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:43:25 2022

@author: Анастасия Рахманина
"""
# задание 1
import math
coord = input ("Введите через запятую координаты вектора")
chisla = []
znach = coord.split (",")
for el in znach:
    chisla.append (int (el))
length = math.sqrt(sum (el**2 for el in chisla))
print (f'длина вектора = {length}')

# задание 3 
# окружность
import matplotlib.pyplot as plt

import math
x = []
y = []
y2 = []

for i in range (-10000,10000):
    R = 1
    x_= i/10000
    x.append(x_)
    y.append (math.sqrt(R**2 - x_**2))
    y2.append (- math.sqrt(R**2 - x_**2))
plt.plot (x,y)
plt.plot (x,y2)
plt.show()

# эллипс
import matplotlib.pyplot as plt

import math
x = []
y = []
y2 = []

for i in range (-10000,10000):
    a = 1
    b = 0.5   
    x_= i/10000
    x.append(x_)
    y.append (math.sqrt((a**2 - x_**2)*(b**2)/a**2))
    y2.append (- math.sqrt((a**2 - x_**2)*(b**2)/a**2))
plt.plot (x,y)
plt.plot (x,y2)
plt.show()

# гипербола
import matplotlib.pyplot as plt

import math
x = []
y = []
y2 = []

for i in range (1,100):
    x_= i/100
    x.append(x_)
    y.append (1/x_)
    
plt.plot (x,y)
plt.plot (x,y2)
plt.show()

# построение параллельных плоскостей
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange (-10, 10, 0.5)
Y = np.arange (-10, 10, 0.5)
X, Y = meshgrid (X, Y)
Z = -3*X + 4*Y
Z1 = -3*X + 4*Y + 10
ax.plot_wireframe(X,Y,Z)
ax.plot_wireframe(X,Y,Z1)

#построение двух поверхностей второго порядка

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange (-10, 10, 0.5)
Y = np.arange (-10, 10, 0.5)
X, Y = meshgrid (X, Y)
Z = X**2 + Y**2
Z1 = X**2 - Y**2
ax.plot_wireframe(X,Y,Z)
ax.plot_wireframe(X,Y,Z1)

# Построение графиков синуса и косинуса с разными параметрами
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3*np.pi, 3*np.pi, 201)
plt.plot (x, 2*np.sin(x+1)+2)
plt.plot (x, 3*np.cos(x+2)-1)
plt.plot (x, 2*np.sin(x)+1)
plt.xlabel('x')
plt.ylabel ('y')
plt.grid (True)
plt.show ()

# Перевод в полярную систему координат
import numpy as np
def polcoord (R,angle):
    X = R*np.cos(angle)
    Y = R*np.sin (angle)
    return (X,Y)
print (polcoord (3,90))

# Окружность в полярных координатах
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1,1,1000)
y = np.sqrt (1-x**2)
plt.polar (x,y)       
plt.show()

# отрезок в полярных координатах 

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1,1,1000)
y = np.sqrt (x+1)
plt.polar (x,y)       
plt.show()

# решение системы уравнений
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2, 3, 201)

plt.plot(x, (np.exp(x)+ x - 1)/x)
plt.plot(x, x**2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1,6) 
plt.grid(True)
plt.show()

from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (x**2 - 1 - y, np.exp(x) + x * (1 - y) - 1)

x1, y1 =  fsolve(equations, (3, 5))
x2, y2 =  fsolve(equations, (-1, 1))
              
print (x1, y1)
print (x2, y2)



