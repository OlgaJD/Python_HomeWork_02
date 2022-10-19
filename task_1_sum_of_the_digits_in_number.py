# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

from decimal import Decimal

def summ (user_number):
    if user_number < 0:
        user_number *= -1

    n1 = int(user_number)
    n2 = Decimal(user_number-n1)
  
    sum1 = 0 ## отдельно считаем сумму цифр в целой части числа 
    while n1 != 0:
        sum1 = sum1 + n1 % 10
        n1 //= 10
    # print(f'Сумма цифр в первой части: {sum1}')

    while n2 %10 !=0:
        n2 *= 10
    # print (f'Округлили дробную часть до целого числа {n2}')

    sum2 = 0 ## отдельно считаем сумму цифр в дробной части числа 
    while n2 != 0:
        sum2 = sum2 + n2 % 10
        n2 //= 10
    # print(f'Сумма цифр в дробной части: {sum2}')

    sum = sum1 + sum2
    return int(sum)

try:
    number = Decimal(input('Введите любое число: '))
    print(f'Сумма цифр в вашем числе равна: {summ(number)}')
except:
    print('Вводите только числа')


    ## Version 2 string

# number = input('Enter number: ')
# sum = 0
# for i in number:
#     if i != '.' and i != '-':
#         sum += int(i)
# print(sum)



