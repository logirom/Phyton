# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

def median(num):
    middle = int(len(array) / 2)
    num.sort()
    print(f'сортированный массив \n {num}')
    if not len(num) % 2:
        return (num[middle - 1] + num[middle]) / 2

    return num[middle]


m = 19
size = 2*m+1
array = []
for i in range(size):
    array.append(random.randint(0, 50))

print(f'исходный массив \n {array}')
print('Медиана:', median(array[:]))

