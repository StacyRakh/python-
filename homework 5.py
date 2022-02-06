# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:37:25 2022

@author: Анастасия Рахманина
"""

# задание 1
firstfile = open("firstfile.txt", "w") #создаем файл
new = str (input ("Введите новую строку, для завершения ввода нажмите enter"))
firstfilelist = [] 
while len (new) > 0: # задаем цикл для добавления новых строк
    firstfilelist.append (new + '\n') # добавляем символ для разделения строк
    new = str (input ("Введите новую строку, для завершения ввода нажмите enter"))
firstfile.writelines (firstfilelist) # записываем данные
firstfile.close()
    
out_f = open("firstfile.txt", "r") # открываем на проверку
for line in out_f:
    print(line)
out_f.close()






# задание 2

stroki = open ('stroki.txt', 'w') # создаем файл
stroki_list = ['неврологическое отделение\n', 
               'реанимация эндотоксикозов\n', 'отделение для суицидентов\n']
stroki.writelines (stroki_list)
stroki.close()
stroki = open ('stroki.txt', 'r')
strokilines = stroki.readlines()
a = len (strokilines) #подсчет символов
print (a)
for el in strokilines: # делим на слова
    el.split (' ')
    print (len (strokilines)) # подсчет слов
    
    
    
    

# задание 3
spisok = open ('spisok.txt', 'w')
spisok_list = ['Соколов 12321.23\n', 
               'Петрова 25345.23\n', 
               'Юзбашев 45768.32\n',
               'Викторов 34268.32\n',
               'Сержантов 10123.32\n',
               'Николаав 43468.32\n',
               'Монахова 12348.32\n',
               'Сеймурова 75678.32\n',
               'Лакан 23342.00\n',
               'Фрейд 34534.32\n'
               ]
spisok.writelines (spisok_list)
spisok.close()
stroki = open ('spisok.txt', 'r') 
strokilines = stroki.readlines()
print (strokilines) # на всякий случай проверила читабельность строк
from statistics import mean
srednee = [] 
for el in strokilines: # разделяем строку на состявляющие
    a = el.split (' ')
    b = float (a [-1]) # обозначаем зп
    if b > 20000.00:
        print (a [0]) # выводим строки при условии
    if b > 0: 
        srednee.append (b) # создали лист, чтобы можно было посчитать среднее по формуле
        c = mean (srednee) # добавили готовую формулу
print (c) # готовая форма
stroki.close ()   






#Задача 4
seasons = open ('seasons.txt', 'w')
seasons_list = ['One - 1\n', 
               'Two - 2\n', 
               'Three - 3\n',
               'Four - 4\n'
               ]
seasons.close ()
opening = open ('seasons.txt', 'r')
new = opening.readlines ()
import shutil
shutil.copyfile ('seasons.txt','newseasons.txt') # копируем содержимое в новый файл
fix = open ('newseasons.txt', 'r')
fixing = fix.readlines ()
next1 = []
for el in fixing:
    a = el.split (' ') # порезали строку на переменные
    if a[0] == "One": # заменяем символы
        a[0] = str ("Один")
        next1.append (a) # создаем новый текст с новым первым словом     
    elif a[0] == "Two":
        a[0] = str ("Два")
        
        next1.append (a)  
    elif a[0] == "Three":
        a[0] = str ("Три")
        
        next1.append (a)  
    elif a[0] == "Four":
        a[0] = str ("Четыре")
        
        next1.append (a) 
next2 = [] 
for el in next1:
    beta = str (' '.join (el))
    next2.append (beta) # добавляем пробелы для переноса строк
print (next2)

imp = open ('newseasons.txt', 'w')
imp.writelines (next2)

fix.close ()
imp.close ()    





# Задача 5
numbers = open ('number.txt', 'w')
numbers_list = '4, 5, 6, 7, 8, 9, 45' # создаем строку
numbers.writelines (numbers_list)
numers = numbers_list.split(', ') 
chisla = []
for el in numers: # превращаем переменные в числа
    chisla.append (int (el)) # добавляем лист для формулы
print (sum (chisla))
numbers.close ()





# задача 6

time = open ('time.txt', 'w') 
time_list = ['Психология: 23 (л) 24 (пр)\n', 
               'Психиатрия: 24 (c) 24 (пр)\n', 
               'Неврология: 24 (л) 24 (с) 144 (пр)\n'
             ]
time.writelines (time_list)
time.close ()

lection = open ('time.txt', 'r') 
table = lection.readlines ()
rasp = {}

for el in table:
    a = el.split (' ') # каждую строку делим
    name = a [0] # называем переменную - ключ
    c = []
    for i in a:
         if i.isdigit() == True: # отбираем цифры
          i = int (i)
          c.append (i)
    bet = sum (c) # считаем в листе сумму отобранных цифр
    subj = {name:bet} # создаем подключи 
    rasp.update(subj) # объединяем в единый ключ
print (rasp)





# Задание 7

money = open ('money.txt', 'w')
money_list = ['Стоматология ООО 12345 2345\n', 
               'Косметология ЗАО 20000 35000\n', 
               'Парикмахерская ОАО 34555 23433\n'
               'Ветеринария ООО 23122 23120'
             ]
money.writelines (money_list)
money.close ()    
summ = open ('money.txt', 'r')
sums = summ.readlines ()
from statistics import mean
sections = {} # словарь с прибылями и убытками
vyruchki = []
for el in sums:
     a = el.split (' ')
     pribyl = float (a [-2])
     izderzh = float (a [-1])
     if pribyl >= izderzh: # в случае прибыли
        vyruch = pribyl - izderzh
        vyruchki.append (vyruch) # создаем лист для средней прибыли
        names = {a[0]:vyruch} # создаем словари для прибыльных
        sections.update (names) # добавляем в общий словарь
           
     if izderzh > pribyl: 
          ubyt = izderzh - pribyl
          ubytki = {a[0]:ubyt} #создаем ключи убытков
          sections.update (ubytki) # по условиям задачи тоже добавляем в список
          
srednee = {'average':mean(vyruchki)} # словарь средней выручки
forjson = [sections,srednee]
import json
with open ('money.txt', 'w') as summ:
    json.dump (forjson,summ)
summ.close() 




#######для удаления файлов с компьютера#####
import os
os.remove ("firstfile.txt")
os.remove ("stroki.txt")
os.remove ("spisok.txt")
os.remove ("newseasons.txt")
os.remove ("seasons.txt")
os.remove ("number.txt")
os.remove ("time.txt")
os.remove ("money.txt")
    