# НЕОБЯЗАТЕЛЬНАЯ ЗАДАЧА
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


def create_new_list(n):
    new_list = ['']*n
    for i in range(n):
        new_list[i] = randint(-n, n)
    return new_list

def create_new_txt_file():
    with open ('file.txt', 'w', encoding='utf-8') as file:
        for _ in range(randint(1, n)):
            file.write(str(randint(0, n-1)) + '\n')
    # print('File created')

def product_of_numbers(some_list):
    result = 1
    print('Числа-позиции из файла: ', end='')
    with open ('file.txt','r', encoding='utf-8') as file:
        file = file.read().splitlines()
        print(file)
        for number in file:
            result *= some_list[int(number)]
    return result

try:
    n = int(input('Введите длину списка: '))
    new = create_new_list(n)
    print (f'Созданный список: {new}')
    create_new_txt_file()
    print(f'Произведение элементов на позициях из файла равно: {product_of_numbers(new)}')
    
except:
    print('Вводите только целые числа')
