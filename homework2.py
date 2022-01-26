# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Задание 1
per = [1, "hello", {567}] # задаем переменную
print (type (per [2])) # выясняем ее тип





# Задание 2
list_2 = list (input ("Напишите любое сложное слово")) 
a = list_2 [-1]
if (len (list_2) % 2) == 1:
  list_2.pop(-1)
  list_2 [ : :2], list_2 [1: :2] = list_2 [1: :2], list_2 [ : :2]  
  list_2.append(a)
if (len (list_2) % 2) == 0:
    list_2 [ : :2], list_2 [1: :2] = list_2 [1: :2], list_2 [ : :2]
print (list_2)





# Задание 3
months = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
monts_list = ['зима', 'весна', 'лето', 'осень']
a = int (input ("Введите номер месяца"))
if a == 1 or a == 2 or a == 12:
    print (months.get(1))
    print (monts_list[0])
elif a == 3 or a == 4 or a == 5:
        print (months.get(2))
        print (monts_list[1])
elif a == 6 or a == 7 or a == 8:
        print (months.get(3))
        print (monts_list[2])
elif a == 9 or a == 10 or a == 11:
        print (months.get(4))
        print (monts_list[3])






# Задание 4
words = str (input ("Напишите несколько слов"))
fix = list (words.split( ))
for ind, el in enumerate (fix, 1):
            if len (el) > 10:
              print (ind, el[0:10])
            else: print (ind, el)






# Задание 5
rate = [7,7,8,9]
rate.sort (reverse  = True)
a = int (input ("Введите переменную"))
for i in range (len(rate)):
   if rate [i] == a:
      rate.insert (i+1,a)
      break
   elif rate [0] < a:
      rate.insert (0, a)
   elif rate [-1] > a:
      rate.append (a)
   elif rate [i] > a and rate [i+1] < a:
      rate.insert (i+1, a)
print (rate)
    
      
      
# Задание 6 (к сожалению, не смогла сделать цикл, 
# чтобы программа каждый раз в конце предлагала ввести еще данные 
# или завершалась)
analytic = {}
n = int (input ("Введите номер товара"))
characters = []
tovary = []
while n >= n:
   characters = dict ({'название': input ("укажите название"), 'цена': input ("укажите цену товара"), 
                       'количество': input ("укажите количество товара"), 'ед': input ("укажите единицу измерения")})
   tovary.append ((n,characters))
   n = n + 1
   analytic = dict({'название': characters.get ('название'), 'цена': characters.get ('цена'), 
                     'количество': characters.get ('количество'), 'ед': characters.get ('ед')})
   print (tovary)
   print (analytic)


    



    
    

      
    
        
    

        
    
