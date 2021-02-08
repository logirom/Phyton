class JustNumber(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"тип данных строка"


def get_number():
    data = input("введите число")
    if not data.isnumeric():
         raise JustNumber(data)
    return int(data)


my_list = []
while True:
    try:
        data = get_number()
        my_list.append(data)
        print(my_list)
    except JustNumber as e:
        if e.data == "stop":
            break
        print(e)

