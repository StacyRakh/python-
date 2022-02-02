# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 23:54:42 2022

@author: Анастасия Рахманина
"""

# Задание № 1

from sys import argv

name, hours, stavka, reward = argv
hours = int(hours)
stavka = int(stavka)
reward = int(reward)
salary = hours * stavka + reward
print (f'заработная плата сотрудника = {salary}')




# №2
example = [34,45,45,65,234,54,54,3,4,49,67]
  
gen = [el for ind, el in enumerate (example) 
       if example [ind - 1] < example [ind]]
print (gen)



# №  3
genes = [el for el in range (20,242) if el%20 == 0 or el%21 == 0]
print (genes)
    



# 4
gen = [4, 4, 5, 5, 32, 123, 16, 32, 124, 42]
genes = [el for el in gen if gen.count (el)==1]
print (genes)





#Задание № 5
chisla = [el for el in range (10,1001)]
from functools import reduce
def umnozh (elem1, elem2):
    a = elem1*elem2
    return a
print (reduce(umnozh, chisla))

# Задание № 6
from itertools import count
for el in count (1):
    if el > 34:
        break
    else:
        print (el)
from itertools import cycle
import untitled1 
print (untitled1.mnozh()) #открытие модуля

from itertools import cycle

print (f'Вам дан список цифр 3, 4, 5, 2, 6, 8, 4, элементы повторяются 8 раз')
c = 0
for el in cycle ([3, 4, 5, 2, 6, 8, 4]):
  if c == 8:
      break
  print (el)
  c = c + 1
import untitled2 #открываем модуль 

# Задание № 7 

from math import factorial
def fact ():
    n = int (input ("Введите число"))
    el = 1
    while el*el != factorial (n):
        el = el + 1
        generator = [el for el in range (1, n+1)]
    yield generator
print (fact())


