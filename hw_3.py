# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# print('Числа: ', list)
# sum = 0
# for i in range(len(list)):
#     if i % 2 !=0:
#         sum += list[i]
# print(f'Сумма чисел с нечетными индексами = ', sum)


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# import random

# number = int(input('Введите размер списка: '))
# start_list = []
# result_list = []

# for i in range(number):
#     start_list.append(random.randint(0, 9))

# for i in range(len(start_list)):
#     while (i<len(start_list)/2) and (number>len(start_list)/2):
#         number = number - 1
#         pr = start_list[i] * start_list[number]
#         result_list.append(pr)
#         i += 1
# print('Список чисел: ', start_list)
# print('Произведение пар чисел: ', result_list)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [2.51014, 25.501, 8.0025, 17, 44.33, 18.292]
# min = list[0]
# max = 0

# for i in range(len(list)):
#     if max < list[i]:
#         max = list[i]
#     if min > list[i]:
#         min = list[i]
# dif = max - min

# print(list)
# print('Min =', min, 'Max =', max)
# # print(round(dif,2))
# print(dif)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number = int(input('Введите число для преобразовывания десятичного числа в двоичное: '))
# ans = " "
# while number != 0:
#     ans += str(number%2)
#     number //=2
# print(ans)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# def Fib(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fib(n-1) + Fib(n-2)

# def NegaFib(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = []
# number = int(input('Введите число: '))
# for e in range(1, number + 1):
#     list.append(Fib(e))
#     list.insert(0, NegaFib(e))
# print(list)