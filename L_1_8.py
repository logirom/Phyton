name = input("Введите свое имя")
surname = input('Введите свою фамилию')
age = int(input('Введите количество полных лет'))
weight = int(input('Введите свой вес (в кг)'))
health_status_good = '- У вас хорошее состояние здоровья'
health_status_average ='- вам следует заняться собой'
health_status_bad = '- вам следует обратится к врачу!'
if age < 30 and (weight > 50 and weight < 120):
print(name,", ",surname,", ", age, ",",health_status_good)
elif (age >= 30 and age <40) and (weight < 50 or weight > 120):
print(name, ", ", surname, ", ", age, ",", health_status_average)
elif age >= 40 and (weight < 50 or weight > 120):
print(name, ", ", surname, ", ", age, ",", health_status_bad)
else:
print(name, ", ", surname, ", ", age, ",", health_status_good)