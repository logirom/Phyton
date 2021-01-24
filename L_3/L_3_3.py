a = int(input('a='))


def func(v, b, c):
    lst = [v, b, c]
    try:
        m = min(lst)
        s = sum(lst)
        return s-m
    except TypeError:
        return "только числа"


print(func(a, 57, 7))