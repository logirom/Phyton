file = open("l53.txt", "r")

lines_init = file.readlines()
lines = map(lambda l: l.split(), lines_init)
lines_filtered = filter(lambda l: len(l) == 2, lines)
average_sal = 0
num = 0
for p in lines_filtered:
    pers = p[0]
    sal = int(p[1])
    if sal < 20000:
        print(f"{pers} has salary less than 20000")
    average_sal += sal
    num += 1
average_sal /= num
print(f"Average salary is {average_sal}")
file.close()
