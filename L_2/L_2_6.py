enter = ""
items = 0
features = list()
while enter == "":
    items = items + 1
    name = input("название товара ")
    price = input("цена товара ")
    number = input("количество товара ")
    features.append((items, {"название товара": name, "цена товара": price, "количество товара": number}))
    enter = input("нажмите клафишу ввод для продолжения или любую клавишу для выходо")
for values in features:
    print(values)
analitics = {"название товара": list(), "цена товара": list(), "количество товара": list()}
for items, value in features:
    for key, val in value.items():
        analitics[key].append(val)
for value in analitics.items():
    print(value)



