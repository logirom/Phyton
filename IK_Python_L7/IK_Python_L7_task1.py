#1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

def buble(array):
    n = 1
    while n < len(array):
        for i in range(len(array)-n):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n += 1
    return array

size = 100
array = [random.randint(-100, 100) for i in range(size)]
print(f'исходный массив \n {array}')

print(f'сортированный массив\n {buble(array)}')


