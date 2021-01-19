stroka = input("ввести строку ")
word = list(stroka.split())
for ind, el in enumerate(word):
    if len(el) > 10:
        print(ind+1, el[0:10])
    else:
        print(ind+1, el)



