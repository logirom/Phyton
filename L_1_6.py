km_start = int(input("км в первый день "))
km_finish = int(input("км через несколько дней "))
days = 1
km = km_start * 0.1 + km_start
while km <= km_finish:
     km = km_start * 0.1 + km
     days = days + 1

print(f"результат будет достигнут через {days} дней")

