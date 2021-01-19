my_list = [(2), "рамы мыла мама", "домыла только", 1.5, {67}]
for index, elements in enumerate(my_list, 1):
    print(f"{index}. {elements} - {type(elements)}")