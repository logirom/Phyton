spisok = list(input("введите значения: "))
index = 0
while index < len(spisok)-1:
        spisok[index], spisok[index+1] = spisok[index+1], spisok[index]
        index = index + 2
print("измененные значения", spisok)
