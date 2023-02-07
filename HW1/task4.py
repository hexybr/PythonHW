#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
#(то есть разломить шоколадку на два прямоугольника).
#Пример:
#3 2 4 -> yes
#3 2 1 -> no

length_of_the_chocolate = int(input('Введите длинну шоколадки: '))
chocolate_width = int(input('Введите ширину шоколадки: '))
slice = int(input('Отломить долек за раз: '))

if slice < length_of_the_chocolate and slice < chocolate_width:
    print('No')
elif slice % length_of_the_chocolate != 0 and slice % chocolate_width !=0:
    print('No')
else:
    print('Yes')