#Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

M = 6
N = 6
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 6)
        b.append(n)
    a.append(b)
print(a)
max = 0
for j in range(M):
    min = a[0][j]  # внутри цикла
    for i in range(N):
        if a[i][j] < min:  # здесь минимальный ищем
            min = a[i][j]
    if max < min:
        max = min
print(max)
