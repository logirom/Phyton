file = open("l56.txt", "r")

numbers = "1234567890 "
dic = {}
for line in file:
    header, nums = line.split(":")
    dic[header] = sum(map(int, "".join([num for num in nums if num in numbers]).split()))
print(dic)
file.close()
