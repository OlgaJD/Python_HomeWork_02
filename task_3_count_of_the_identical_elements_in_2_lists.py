# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

def count_lines_in_line (first_str, second_str):
    count = 0
    for i in range(len(first_str)):
        if first_str[i:i+len(second_str)] == second_str:
            count +=1
            i += len(second_str)
        else:
            i += 1
    return count

first_s = input('Введите строку в которой будем искать: ')
second_s = input('Что ищем? ')
print(count_lines_in_line(first_s, second_s))

