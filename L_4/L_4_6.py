from itertools import count, cycle

def generator(start, end):
    for el in count(start):
        if el > end:
            break
        yield el

n = int(input("введите стартовое число "))
el_1 = int(input("введите последнее число "))
print(f"число начиная с {n} по {el_1}")

#quit = input()
#    if quit == "q":
#        break

my_list = list(generator(n, el_1))
print(my_list)
liter = cycle(my_list)
i = 0
for elem in liter:
    if i >= len(my_list)*2:
        break
    i += 1
    print(elem, end=" ")




