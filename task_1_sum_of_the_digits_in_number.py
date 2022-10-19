# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

from decimal import Decimal

    ## Version 1 algorithm

def summ (number):
    if number < 0:
        number *= -1
    n_fractional_part = number-int(number)
    while n_fractional_part %10 !=0:
        n_fractional_part *= 10
    number = n_fractional_part + int(number)
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return int(sum)

try:
    user_number = Decimal(input('Введите любое число: '))
    print(f'Сумма цифр в вашел числе равна: {summ(user_number)}')
except:
    print('Вводите только цифры')


    ## Version 2 string

# number = input('Enter number: ')
# sum = 0
# for i in number:
#     if i != '.' and i != '-':
#         sum += int(i)
# print(sum)



