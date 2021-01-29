from random import randint

file = open("l55.txt", "w+")
for _ in range(randint(15, 99)):
    file.write(f"{randint(1, 999)} ")
file.seek(0)
txt = file.readline()
nums = map(int, txt.split())
s = sum(nums)
print(f"Sum is {s}")
file.close()

