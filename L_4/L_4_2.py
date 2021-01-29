from random import randint
from sys import argv


def inital_generator(min, max, n):
    for el in range(n):
        yield randint(min, max)


def generator(spisok):
    spisok_el = spisok[0]
    for el in spisok:
        if el > spisok_el:
            yield el
        spisok_el = el


_, min, max, num = argv
spisok_init = list(inital_generator(int(min), int(max), int(num)))
spisok_1 = list(generator(spisok_init))
print(f"начальный список {spisok_init}\n результат {spisok_1}")


