file = open("l54.txt", "r")
file_out = open("l54out.txt", "w")

russians = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять"]
for line in file:
    pair = line.split(" - ")
    if len(pair) != 2:
        continue
    num = int(pair[1])
    russ_word = russians[num]
    file_out.write(f"{russ_word} - {num}\n")
file.close()
file_out.close()
