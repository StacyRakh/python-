# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:15:59 2022

@author: Анастасия Рахманина
"""

# Задание 1

import time

class TrafficLight:
    # атрибуты класса
    __color = ["red", "yellow", "green"]
    
    # метод класса 
    def running(self):
        el = 0
        for el in range(3):
            print(f'TrafficLight mode is { TrafficLight.__color[el]}')
            if el == 0:
                time.sleep(7)
            if el == 1:
                time.sleep(2)
            if el == 2:
                time.sleep(3)


tl = TrafficLight()
tl.running()








# задание 2

# задаем класс
class Road:
    def massroad(self,length, width, mass,square):
        self.__length = length
        self.__width = width
        self.mass = mass
        self.square = square
        print (f'масса асфальта {self.__length}*{self.__width}*{self.mass}*{self.square}/1000 = {self.__length* self.__width*self.mass*self.square/1000} т)')
    
     
r = Road ()
# задаем переменные
r.massroad (int(input ('Введите длину дороги в метрах')),
           int (input ('Введите ширину дороги в метрах')),
            int (input ("Введите массу дороги")), 
            int (input ("Введите толщину дороги")))





# задание 3
class Worker:

    # задаем метод

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

# дочерний класс

class Position (Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    
    # задаем методы

    def get_full_name(self):
        return " ".join([self.name, self.surname])
    
    def get_total_income(self):
        # достаем из словаря данные для дохода
        return self._income.get('wage') + self._income.get('bonus')
        

p = Position ('Peter', 'Sokolov', 'surgeon', 25000, 72000)
    
print(p.get_full_name())
print(p.position)
print(p.get_total_income())






# Задание 4
# базовый класс
class Car:
     
    # конструктов с переменными
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы класса
    def go(self):
        return f'{self.name} начал(а) движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} {self.speed} км.ч'
 
# дочерний класс
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed} км.ч')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой'
        # перезагрузка метода с условием     

# дочерний класс
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

# дочерний класс
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed} км.ч')

        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой'
         # перезагрузка метода с условием 

# дочерний класс
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


# экземпляры и вызов методов
nissan = TownCar(60, "black", "Qashqai", False)
bugatti = SportCar (150, "red", "Vierron", False)
man = WorkCar(45, "blue", "1401", False)
shkoda = PoliceCar(55, "White", "Octavia", True)
print (nissan.go())
print (f'какая скорость Бугатти? {bugatti.speed}')
print (man.turn_right())
print (man.show_speed())






# Задание 5

# создаем класс
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

# создаем дочерние классы
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это {self.title}. Теперь вы рисуете ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это {self.title}. Теперь вы рисуете карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это {self.title}. Теперь вы рисуете маркером'
    
p = Pen("ручка")
c = Pencil ("карандаш")
m = Handle ("маркер")
print (p.draw())
print (c.draw())
print (m.draw())