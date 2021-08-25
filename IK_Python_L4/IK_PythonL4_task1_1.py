#%%
# Это решение медленнее, чем второе, в обоих случаях сложность N,рекурсий нет
# Найти сумму n элементов следующего ряда
# чисел: 1, -0.5, 0.25, -0.125,… Количество
# элементов (n) вводится с клавиатуры.

import cProfile
def sumn(n):
    a = 1
    sum_a = a
    for i in range(0, n):
        a = a / 2 * -1
        sum_a = sum_a + a
    return sum_a

n = int(input("Введите n..."))
print(sumn(n))

cProfile.run('sumn(n)')
#999 loops, best of 5: 2 usec per loop for n =9
#999 loops, best of 5: 23.5 usec per loop для n99
#999 loops, best of 5: 237 usec per loop for n=999

#4 function calls in 0.000 seconds, n =9, 99, 999
#4 function calls in 0.002 seconds n =9999




