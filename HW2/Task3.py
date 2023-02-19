#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))
list_of_degrees = []
for i in range(0, n):
    if 2**i <= n:
       list_of_degrees.append(2**i)
print(list_of_degrees)
