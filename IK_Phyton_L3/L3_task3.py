#В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import random
mn = 0
mx = 0
M = 9
arr = [0] * M
for k in range(M):
    arr[k] = int(random()*9)
    print(arr[k], end=' ')
for k in range(M):
    if arr[k] < arr[mn]:
        mn = k
    elif arr[k] > arr[mx]:
        mx = k
print(f' \n{mn+1}\n {arr[mn]}\n {mx+1}\n {arr[mx]}')

