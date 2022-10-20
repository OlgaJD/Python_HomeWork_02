# Реализуйте алгоритм перемешивания списка.

import random 

def create_list():
    new_list = [random.randint(0,10) for _ in range(int(input('Введите длину списка: ')))]
    return new_list

rand_list = create_list()
print(rand_list)
random.shuffle(rand_list)
print(rand_list)




