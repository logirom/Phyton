from abc import ABC, abstractmethod

class Store:
    __items = {"printers": list(), "scaner": list(), "xerox": list()}
    def place(self, item):
        if isinstance(item, Printer):
            self.__items["printers"].append(item)
        elif isinstance(item, Scaner):
            self.__items["scaner"].append(item)
        elif isinstance(item, Xerox):
            self.__items["xerox"].append(item)
        else:
            raise Exception("unknown type")

    def move(self, item_type, number):
        if self.__items[item_type] < number:
            raise Exception("not enough")
        to_move = self.__items[item_type][:number]
        self.__items[item_type] = self.__items[item_type][number:]
        return to_move

    def __str__(self):
        return f"принтеров: {len(self.__items['printers'])}\n сканер: {len(self.__items['scaner'])}\n" \
               f"xerox: {len(self.__items['xerox'])}"


class OrgTech(ABC):
    def __init__(self, price):
        self.price = price


class Printer(OrgTech):
    def __init__(self, price, type):
        super().__init__(price)
        self.type = type


class Scaner(OrgTech):
    def __init__(self, price, ishandscaner):
        super().__init__(price)
        self.ishandscaner = ishandscaner


class Xerox(OrgTech):
    def __init__(self, price, color):
        super().__init__(price)
        self.colore = color


printers_number = int(input("введите количество принтеров"))
scaners_number = int(input("введите количество сканеров"))
xerox_number = int(input("введите количество ксероксов"))
store = Store()
for i in range(printers_number):
    store.place(Printer(1999, 'laser'))
for i in range(scaners_number):
    store.place(Scaner(999, True))
for i in range(xerox_number):
    store.place(Xerox(699, 'bw'))

print(store)