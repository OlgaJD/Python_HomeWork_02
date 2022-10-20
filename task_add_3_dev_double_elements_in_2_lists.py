# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

import random

def create_list():
    new_list = [random.randint(0,10) for _ in range(int(input('Введите длину списка: ')))]
    return new_list

def find_duplicate_elements(first_list, second_list):
    duplicate_list = []
    for i in range(len(first_list)):
        if first_list[i] in second_list:
            duplicate_list.append(first_list[i])
    return duplicate_list

rand_list1 = create_list()
rand_list2 = create_list()
print(f'Первый список: {rand_list1}')
print(f'Второй список: {rand_list2}')
print(f'Пересечение элементов: {(find_duplicate_elements(rand_list1, rand_list2))}')
