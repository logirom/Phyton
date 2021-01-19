month = int(input('введите месяц '))
list_1 = [12, 1, 2]
list_2 = [3, 4, 5]
list_3 = [6, 7, 8]
list_4 = [9, 10, 11]
year_time = {"zima": list_1, "spring": list_2, "summer": list_3, "autumn": list_4}
for (key, list_n) in year_time.items():
    if month in list_n:
        print(f"{month} месяц года это", key)





