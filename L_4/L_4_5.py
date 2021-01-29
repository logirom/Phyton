from functools import reduce


def multpl(el1, el2):
    return el1*el2


my_list = [el for el in range(100, 1001, 2)]
my_list_result = reduce(multpl, my_list)
print(f"исходная последовательность\n{my_list}\n результат умножения\n {my_list_result}")