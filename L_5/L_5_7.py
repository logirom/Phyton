import json
file = open("l57.txt", "r")

average = 0
i = 0
pnls = {}
for line in file:
    firm, tp, pstr, lstr = line.split()
    pnl = int(pstr) - int(lstr)
    pnls[firm] = pnl
    if pnl > 0:
        i += 1
        average += pnl
print(f"Average income is {(average / i) if i > 0 else 0}")
avg_obj = {"average_profit": average}
file.close()
with open("l57.json", "w") as outf:
    json.dump([pnls, avg_obj], outf, ensure_ascii = False, indent = 4)

