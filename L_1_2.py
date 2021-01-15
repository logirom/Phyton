sec = int(input("Введите время в секундах "))
min = sec // 60
sec_res = sec % 60
hrs = min // 60
min_res = min % 60
print (f"{hrs}:{min_res}:{sec_res}")
