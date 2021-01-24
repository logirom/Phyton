a = int(input("введите число "))
b = int(input("введите число "))

def division(a1, b1):
    try:
        c = a1 / b1
        return round(c, 4)
    except ZeroDivisionError:
        return "деление на ноль запрещено"
print(division(a, b))


