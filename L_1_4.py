number = int(input("ввести целое положительное число "))
dig = 0
num = number
while num > 0:
    dig_dig = num % 10
    if dig_dig > dig:
        dig = dig_dig
        if dig == 9:
            break
    num = num // 10
print(f"наибольшая цифра в числе {number} равна {dig}")