str = input("ведите слово латинскими буквами:\n")


def int_func(w):
    chars = 0
    for char in w:
        if 97 <= ord(char) <= 122:
            chars = chars + 1
    if chars == len(w):
        word = w.capitalize()
        return word
    else:
        print("только латинские символы: \n")
        return ""
result = ""
for word in str.split(" "):
        result = result + " " + int_func(word)

print(result)