# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 16:19:40 2022

@author: Анастасия Рахманина
"""

# задание 1
import random as rnd 

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.strings = len (matrix)
        self.columns = len (matrix [0])
        
    def __str__(self):
        out = str ('')
        for row in self.matrix:
            out += " ".join ([str(num) for num in row]) + "\n"
            return out
    
    def __add__(self, new):
        new_matrix = [[]]
        new_strings = len (new.matrix)
        new_columns = len (new.matrix [0])
        if self.strings == new.strings and self.columns == new.columns:
            new_matrix = [[self.matrix [j][i] + new.matrix [j][i] 
                           for i in range (self.strings)] for j in 
                          range (self.columns)]
        else:
            print ("Матрицы не совпадают")
        return Matrix(new_matrix)

strings = int (input ("ВВедите количество строк в матрице"))
columns = int (input ("Введите количество столбцов"))
matricy = [[rnd.randint (0,20) for _ in range (columns)]
           for x in range (strings)]
m = Matrix (matricy)
print (f'Матрица: \n{m}')
new_matricy = [[rnd.randint (0,20) for _ in range (columns)]
           for x in range (strings)]
newm = Matrix (new_matricy)
print (f'Новая матрица \n {newm}')
print (f'При сложении матриц получается \n {m + newm}')     

# задание 2

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def coat_square (self):
        return self.size / 6.5 + 0.5

    def suit_square (self):
        return self.height * 2 + 0.3

    @property
    def sum_square (self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.coat_square = self.size / 6.5 + 0.5

    def __str__(self):
        return f'Площадь на пальто {self.coat_square}'


class Suit (Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.suit_square = self.height * 2 + 0.3

    def __str__(self):
        return f'Площадь на костюм {self.suit_square}'

coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(suit.sum_square)
    


# задание 3

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, new):
        return Cell(self.quantity + new.quantity)

    def __sub__(self, new):
       
        return self.quantity - new.quantity if (self.quantity - new.quantity) > 0 else print('нельзя выполнить')

    def __mul__(self, new):
        
        return Cell(int(self.quantity * new.quantity))

    def __truediv__(self, new):
      
        return Cell(round(self.quantity // new.quantity))


    def make_order(self, cellsorder):
        row = ''
        for i in range(int(self.quantity / cellsorder)):
            row += f'{"*" * cellsorder} \\n'
        row += f'{"*" * (self.quantity % cellsorder)}'
        return row

cells1 = Cell(33)
cells2 = Cell(32)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1 / cells2)
