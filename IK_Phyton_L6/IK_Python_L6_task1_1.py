# Найти сумму n элементов следующего ряда
# чисел: 1, -0.5, 0.25, -0.125,… Количество
# элементов (n) вводится с клавиатуры.

#%%
import sys
import ctypes
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


def show_size(var_list, level = 0):
    sum_ = 0
    if hasattr(var_list, '__iter__'):
        for x in var_list:
            sum_ += show_size(x, level + 1)
    elif isinstance(var_list, str):
        for x in var_list:
            sum_ += show_size(x, level + 1)
    else:
        sum_ += sys.getsizeof(var_list)
    print('\t'*level, f'type = {var_list.__class__}, size={sum_}, object={var_list}')
    return sum_


n = int(input("Введите n..."))
lst = list(getsequence(n))
res = show_size((lst, n))
print(f'Под переменные задействованно {res} байт памяти')
print(sumsequence(lst))

# n=5
#		 type = <class 'int'>, size=28, object=1
# 		 type = <class 'float'>, size=24, object=-0.5
# 		 type = <class 'float'>, size=24, object=0.25
# 		 type = <class 'float'>, size=24, object=-0.125
# 		 type = <class 'float'>, size=24, object=0.0625
# 		 type = <class 'float'>, size=24, object=-0.03125
# 	 type = <class 'list'>, size=148, object=[1, -0.5, 0.25, -0.125, 0.0625, -0.03125]
# 	 type = <class 'int'>, size=28, object=5
#  type = <class 'tuple'>, size=176, object=([1, -0.5, 0.25, -0.125, 0.0625, -0.03125], 5)
# Под переменные задействованно 176 байт памяти
# 0.65625
#
# Process finished with exit code 0
