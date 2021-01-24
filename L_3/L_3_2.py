name = input('Введите имя: ')
family = input('Введите фамилию: ')
years = input('Введите возраст: ')
town = input('Введите город проживания: ')
email = input('Введите email: ')

def person(**kwargs):
    result = f'{name}, {family}, {years} года рождения, проживает в городе {town}, e-mail {email}'
    return result


p = person(name=name, family=family, years=years, town=town, email=email)
print(p)
