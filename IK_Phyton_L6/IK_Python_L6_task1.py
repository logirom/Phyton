import sys
import ctypes

def sumn(n):
    a = 1
    sum_a = a
    for i in range(0, n):
        a = a / 2 * -1
        sum_a = sum_a + a
    return sum_a

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
res = show_size(n)

print(f'Под переменные задействованно {res} байт памяти')
print(sumn(n))
# второй вариант
print(ctypes.string_at(id(n)), sys.getsizeof(n))
print(ctypes.string_at(id(sumn)), sys.getsizeof(sum))


# Введите n...5
#  type = <class 'int'>, size=28, object=5
# Под переменные во втором случве задействованно 28 байт памяти
# 0.65625
# b'k' 28
# b'\x01' 72 байт под код функции
