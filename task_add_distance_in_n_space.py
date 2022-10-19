# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

import math

def distance (n, a, b):
    dis = float()
    for i in range(n):
        dis = dis + ((b[i]-a[i])**2)
    dis = round(math.sqrt(dis), 3)
    return dis

def list_with_coordinates_of_point (n):
    coordinate_list = [''] * n
    for i in range(n):
        coordinate_list[i] = (float(input(f'Введите координату по оси {i+1} для точки: ')))
    return coordinate_list

try:
    n = int(input('Введите размерность пространства : '))
    print('Первая точка')
    a = list_with_coordinates_of_point (n)
    print('Вторая точка')
    b = list_with_coordinates_of_point (n)
    print(f'Расстояние между точками равно: {distance(n, a, b)}')
except:
    print('Надо вводить только целое число')