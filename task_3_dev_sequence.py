# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

## Version 1

def create_list(n):
    new_list = []
    for i in range(1, n+1):
        new_list.append(round((1+1/i)**i, 3))
    return new_list

def sum_values_some_list(some_list):
    sum = 0
    for i in some_list:
        sum+=i
    return sum

try:
    n = int(input('Enter integer: '))
    print(f'Summ of elements: {sum_values_some_list(create_list(n))}')
except:
    print('Invalid conditions entered, enter only integers:')

## Version 2

# n = int(input('Enter integer: '))
# sum = 0 
# for i in range (1, n+1):
#     sum += (1+1/i)**i
# print(f'Sum of elements: {sum}')