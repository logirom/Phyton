from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate(self):
        pass

    def __add__(self, other):
        return self.calculate() + other.calculate()


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def calculate(self):
        return round(size / 6.5 + 0.5)


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    def calculate(self):
        return round((2 * height + 0.3)/100)


size = int(input("введите размер пальто "))
height = int(input("введите рост для костюма "))

coat = Coat(size)
costume = Costume(height)
print(coat + costume)
