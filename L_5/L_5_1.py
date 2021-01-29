file = open("l51.txt", "w")
while True:
    s = input()
    if not s:
        break
    file.write(s)
    file.write("\n")
file.close()
