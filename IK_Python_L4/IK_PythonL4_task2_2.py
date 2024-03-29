# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».
#решето Эратосфера
import cProfile

n = int(input("n = "))

# список заполняется значениями от 0 до n
a = []
for i in range(n + 1):
    a.append(i)

# Вторым элементом является единица, которую не считают простым числом забиваем ее нулем.
a[1] = 0

# начинаем с 3-го элемента
i = 2
while i <= n:
    # Если значение ячейки до этого не было обнулено, в этой ячейке содержится простое число.
    if a[i] != 0:
        # первое кратное ему будет в два раза больше
        j = i + i
        while j <= n:
            # это число составное, поэтому заменяем его нулем
            a[j] = 0
            # переходим к следующему числу, которое кратно i (оно на i больше)
            j = j + i
    i += 1

# Превращая список во множество, избавляемся от всех нулей кроме одного.
a = set(a)
# удаляем ноль
a.remove(0)
print(a)
cProfile.run('a')
