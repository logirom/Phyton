file = open("l52.txt", "r")

lines = filter(lambda l: l,  file.readlines())
i = 0
for line in lines:
    words = line.split()
    print(f"line {i+1}: {len(words)} words")
    i += 1
print(f"Lines number {i}")
file.close()