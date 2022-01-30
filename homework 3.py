# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Задание 1 
def delenie (): # Задаем функцию
    try:
        a = float (input ("введите первое число"))
        b = float (input ("введите второе число"))
        otv = a / b
        return (otv)
    except ZeroDivisionError:  #исключаем вариант деления на ноль
        b == 0
        return (print ("на ноль делить нельзя")) # выдаем ответ-пояснение выводу None 
otv1 = delenie ()
print (otv1)

# Задание 2
name = input ("Введите Ваше имя") 
surname = input ("Введите Вашу фамилию")
ybirth = input ("Введите год рождения")
city = input ("Введите город проживания")
mail = input ("ВВедите Ваш e-mail")
phone = input ("Введите номер телефона")
def imens (name,surname,ybirth,city,mail,phone):
   data = ' '.join ([name, surname, ybirth, city, mail, phone]) # создаем строку
   return data
print (imens (name,surname,ybirth,city,mail,phone))

# Pадание 3
a = int (input ("Введите число 1"))
b = int (input ("Введите число 2"))
c = int (input ("Введите число 3"))

def delen (a,b,c):
    d = [a,b,c] # объъект можно не задавать, но это проще, чем дублировать параметры
    
    if c == min (d):
        return a+b 
    elif b == min (d):
         return a+c
    elif a == min (d):
        return b+c 
print (delen (a,b,c))

# задание 4
x = float (input ("Введите любое положительное число"))
y = int (input ("Введите целое отрицательное число"))
def stepen (x,y): 
    return (x**y) # задаем функцию через **
print (stepen (x,y))

x = float (input ("Введите любое положительное число"))
y = int (input ("Введите целое отрицательное число"))
def stepen (x,y):
    a = str (x) # преобразуем в строку, чтобы умножение на число было ее длиной
    while len (a*y) != y: 
        x = 1/(x*x) #  формула возведения в отрицательную степень
        return (x)
print (stepen (x,y))

# задание 5
def cycle ():
    numbers = (input ("Введите новое число или символ b для выхода")).split (' ')
    while numbers.count('b') == 0: # пока у нас только числа, проходимм цикл
        for el in range (len(numbers)):
          numbers [el] = int (numbers [el]) 
        new = input ("Введите новое число").split (' ')
        numbers == numbers.extend (new) # прибавляем новое значение)
    numbers.pop (-1) # если новая строка оканчивается символом или состоит из него
    for el in range (len(numbers)): # убираем его 
      numbers [el] = int (numbers [el]) 
    obj = sum (numbers) # складываем остатки
    return (obj)
print (cycle ())


# задание 66,7
a = str (input ("напишите любое слово на латинице с маленькой буквы"))
def int_func ():
    transl = a.title()
    return transl
print (int_func())

a = str (input ("напишите список слов"))
print (int_func ())
    
    
    