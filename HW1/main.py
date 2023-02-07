#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

digit = int(input('Введите число: '))
digit = abs(digit)
sum = 0

while (digit > 0):
    sum = sum + digit % 10
    digit = digit / 10
sum = int(sum)
print(f'Сумма цифр в числе = {sum}')
