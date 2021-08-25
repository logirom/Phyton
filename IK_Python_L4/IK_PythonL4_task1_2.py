# Найти сумму n элементов следующего ряда
# чисел: 1, -0.5, 0.25, -0.125,… Количество
# элементов (n) вводится с клавиатуры.

#%%
import cProfile

def getsequence(n):
    a = 1
    yield a
    for i in range(0, n):
        a = a / 2 * -1
        yield a


def sumsequence(seq):
    s = 0
    for a in seq:
        s = s + a
    return s


n = int(input("Введите n..."))
seq = list(getsequence(n))

print(seq)
print(sumsequence(seq))
cProfile.run('sumsequence(seq)')
# не смогла разобраться почему timeit не отрабатывает пишет что функция не определена, хотя программа работает
#4 function calls in 0.000 seconds, n =9, 99
#4 function calls in 0.000 seconds n = 999
#4  4 function calls in 0.001 seconds n = 9999
