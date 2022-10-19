# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    factorial_list = []
    result = 1
    for i in range(1, n + 1):
        result *= i
        factorial_list.append(result)
    return factorial_list 

try:
    n = int(input('Enter number: '))
    print(factorial(n))
except:
    print('Enter only positive integers')