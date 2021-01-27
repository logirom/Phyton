from sys import argv


def sal(n_hrs, slr, b):
    return n_hrs * slr + b


try:
    script_name, number_hours, salary, bonus = argv
    result = sal(int(number_hours), int(salary), int(bonus))
    print("ваша зарплата ", result)
except ValueError:
    print("не правильные параметры")





