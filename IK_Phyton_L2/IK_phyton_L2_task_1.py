# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.После выполнения вычисления программа не
# завершается, а запрашивает новые данные для вычислений.За вершение программы дол жно при
# вводе символа '0' в качестве знака операции.Если пользователь вводит неверный знак
# (не  '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать
# знак операции.Также она сообщать пользователю о невозможности деления на ввел его в качестве делителя

print("Ноль в качестве знака операции завершит работу программы")
a = float(input("a="))
while True:
    s = input("Знак (+,-,*,/): ")
    if s == 0:
        break
    if s in ('+','-','*','/'):
        b = float(input("b="))
        if s == '+':
            print(f'a+b = {a+b}')
        elif s == '-':
            print(f'a-b = {a-b}')
        elif s == '/':
            if a != 0:
                print(f'a/b = {a/b}')
            else:
                print("Деление на ноль!, введите знак операции")
        if s == '*':
            print(f'a*b = {a * b}')