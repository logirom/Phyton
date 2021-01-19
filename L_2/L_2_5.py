score = [7, 5, 5, 5, 3, 2, 1]
new_el = int(input("введите бал "))
for ind, el in enumerate(score):
    if new_el > el:
        score.insert(ind, new_el)
        break
if new_el < score[-1]:
    score.append(new_el)
print(score)
