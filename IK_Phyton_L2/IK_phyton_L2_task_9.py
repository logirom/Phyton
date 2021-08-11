# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Bывести на экран это число и сумму его цифр.
print("введите числа")
n = int(input())
n1 = int(input())
suma = 0
suma1 = 0
m = n
m1 = n1
while m > 0:
    number = 0
    number = n % 10
    if number > 0:
        suma += number
    m = m // 10
while m1 > 0:
    number1 = 0
    number1 = n % 10
    if number1 > 0:
        suma1 += number1
    m1 = m1 // 10

if suma1 > suma:
    print(f'максимальную суммa цифр {suma1} имеет число {n1} ')
elif suma1 < suma:
    print(f'максимальную суммa цифр {suma} имеет число {n}')
else:
    print(f'сумма цифр равна {suma} имеют оба числа {n, n1}')
