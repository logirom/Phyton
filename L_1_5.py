gain = float(input("введите вашу выручку "))
outlay = int(input("введите ваши расходы "))
profit = gain - outlay
if profit > 0:
    n = int(input("введите колчество сотрудников "))
    profit_n = profit / n
    print("доход на сотрудника", profit_n)
elif profit < 0:
    print(f"прибыли нет, ваши потери {profit}")
else:
    print("ноль")



