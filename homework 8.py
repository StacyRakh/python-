# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:10:51 2022

@author: Анастасия Рахманина
"""

#задание 1

class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def chisla(cls, date):
        my_date = []

        for i in date.split("."):
            if i != '.': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid (date):
        my_date = []

        for i in date.split("."):
            if i != '.': my_date.append(i)

        if 1 <= int (my_date [0]) <= 31:
            if 1 <= int (my_date [1]) <= 12:
                if 2022 >= int (my_date [2]) >= 0:
                    return f'Все верно'
                else: 
                    return f'данные введены неверно'
               



today = Data('11.01.2022')
print(today)
print (Data.chisla("11.01.2020"))
print (Data.valid ("11.01.2023"))


# задание 2

class ZeroExcept:
    def __init__ (self, chisl, znam):
        try:
            res = chisl/znam
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        else:
            print(f"Все хорошо. Результат - {res}")
        finally:
            print("Программа завершена")


z = ZeroExcept(5, 0)
print (z)

# задание 3

class error ():
    def choice (self):
        spisok = []
        new = str (input ("Введите новый символ и enter для выхода"))
        while len (new) > 0:
            if new.isdigit() == True:
                spisok.append(new)
         
            else:
                print (f'это не число')
               
            new = input ("Введите новый символ и enter для выхода")
                 
        print(spisok)    
                
a = error()
a.choice()               
        


# задания 4-6
class Warehouse ():
    def __init__(self):
        self.rooms = {"printer": 15, "scaner": 13, "xerox": 8}

    def priem(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == 'printer':
            self.rooms["printer"] = int(self.rooms.get("printer")) + self.quantity
        if self.name == 'scaner':
            self.rooms["scaner"] = int(self.rooms.get("scaner")) + self.quantity
        if self.name == 'xerox':
            self.rooms["xerox"] = int(self.rooms.get("xerox")) + self.quantity
        print(f'Принят товар {self.name}  в количестве {self.quantity} шт. Актуальное количтество техники {self.rooms}')

    def spisanie(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == 'printer':
            self.rooms["printer"] = int(self.rooms.get("printer")) - self.quantity
        if self.name == 'scaner':
            self.rooms["scaner"] = int(self.rooms.get("scaner")) - self.quantity
        if self.name == 'xerox':
            self.rooms["xerox"] = int(self.rooms.get("xerox")) - self.quantity
        print(f'Товар  {self.name} списан со склада в количестве {self.quantity} шт. Актуальное количетство товара {self.rooms}')

class Orgtech():
    def __init__(self, name, serial_number, price, color):
        self.name = name
        self.serial_number = serial_number
        self.price = price
        self. color = color
       

class Printer (Orgtech):
    def __init__(self, name, serial_number, price, color, printtype):
        super().__init__(name, serial_number, price, color)
        self.printtype = printtype
        print (f'Принтер {self.name} с серийным номером {self.serial_number} цвета {self.color} по цене {self.price} имеет тип печати {self.printtype}')

class Scaner(Orgtech):
    def __init__(self, name, serial_number, price, color, place):
        super().__init__(name, serial_number, price, color)
        self.place = place
        print (f'Сканер {self.name} с серийным номером {self.serial_number} цвета {self.color} по цене {self.price} для пользования {self.place}')
class Xerox (Orgtech):
    def __init__(self, name, serial_number, price, color, multi):
        super().__init__(name, serial_number, price, color)
        self.multi = multi
        print (f'Ксерокс {self.name} с серийным номером {self.serial_number} цвета {self.color} по цене {self.price} имеет вид {self.multi}')

p = Printer('xp', 12354, 2500, 'черный', 'лазерный')
s = Scaner('lg', 46857, 7000, 'белый', 'офис')
x = Xerox('dell', 9474, 12000, 'металик', 'встроен сканер')
w = Warehouse()
w.priem("printer", 4)
w.spisanie("scaner", 2)


# задание 7

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a} + {self.b * other.a + self.a*other.b}*i+ {self.b * other.b} *i *i'

  


z_1 = ComplexNumber(2, -1)
z_2 = ComplexNumber(1, 5)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)