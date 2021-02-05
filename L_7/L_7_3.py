class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number <= other.number:
            raise ValueError()
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, order):
        rows_number = self.number // order
        row = "*" * order
        row = row + "\n"
        row = row * rows_number
        last_number = self.number % order
        if last_number > 0:
            row = row + ("*" * last_number)
        return row


n = Cell(int(input("how many cells in cell")))
o = int(input("what is order"))
print(n.make_order(o))
n1 = Cell(int(input("how many cells in second cell")))
n3 = n * n1
print(n3.number)

