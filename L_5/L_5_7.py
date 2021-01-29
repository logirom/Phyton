file = open("l57.txt", "r")

average = 0
i = 0
for line in file:
    firm, tp, pstr, lstr = line.split()
    income = int(pstr) - int(lstr)
    if income > 0:
        i += 1
        average += income
print(f"Average income is {(average / i) if i > 0 else 0}")
file.close()

