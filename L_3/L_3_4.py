a = float(input('введите целое положительное число '))
b = int(input('ведите целое отрицательное число '))


def func(x, y):
    result = x ** y
    return f"результат возведения x в степень y равен {round(result, 4)}"


def func1(x, y):
    result1 = 1
    l = range(abs(y))
    for _ in l:
        result1 = result1/x
    return f"результат возведения x в степень y равен {round(result1, 4)}"


print(func(a, b), func1(a, b))



