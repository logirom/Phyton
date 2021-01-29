from functools import reduce


def fact(n):
    return reduce(lambda x, y: x * y, list(el if el > 0 else 1 for el in range(n + 1)))


number = int(input("Число "))
for el in range(1, number + 1):
    print(f"{el}! = {fact(el)}")