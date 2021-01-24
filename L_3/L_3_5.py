def funct(a, sum_n):
    result = 0
    for n in a:
       if n == "@":
            print(result + sum_n)
            exit(0)
       else:
           try:
               i = int(n)
               result = result + i
           except ValueError:
              result = result
    return result + sum_n


sum_num = 0
while True:
    str = list(input('введите числа').split(" "))
    sum_num = funct(str, sum_num)
    print(sum_num)
