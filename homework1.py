e = int (input ('Сколько дней Вы в отпуске'))
d = str (input ("Введите Ваш снилс без пробелов и тире"))
zapr = float (e * 0.6)
print (zapr)
print (f"Вы получите {zapr} тысяч")



# Задание 2

time = int (input ("Введите время в секундах"))
hours = int (time // 3600)
mins = int ((time % 3600) // 60)
secs = int ((time % 3660) % 60)
print (f'{hours}.{mins}.{secs}')    





# Задание 3

n = int (input ("Введите целое число:"))
a = n + 10*n + n + 100*n + 10*n + n
print (a)

# Задание 4
chis = int (input ("Введите целое число:"))
tsifra = chis % 10
chis = chis // 10
while chis > 0:
    if chis % 10 > tsifra:
        tsifra = chis % 10
    chis = chis // 10
print (tsifra)





# Задание 5 
vyr = float (input ("Введите значение выручки:"))
izd = float (input ("Введите значение издержек:"))
if vyr > izd:
    print ("Выручка больше издержек") 
    prib = float (vyr - izd)
    rent = float (prib / vyr)
    kol = (int (input ("Введите количество сотрудников")))
    pribone = float (prib / kol)
if izd > vyr:
    print ("Издержки больше выручки")
    
    
    
    

# Задание 6
a = float (input ("Сколько вы пробежали в 1 день:"))
b = float (input ("Сколько вы хотите пробежать:"))
i = 1
while a < b:
    a = 1.1 * a
    i = i + 1
if a >= b:
    print (i)

    
    