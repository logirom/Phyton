class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        z_1 = ComplexNum(self.real + other.real, self.imag + other.imag)
        return z_1

    def __mul__(self, other):
        z_2 = ComplexNum((self.real * other.real - (self.imag * other.imag)), (self.imag * other.real))
        return z_2

    def __str__(self):
        return f"{self.real} + {self.imag} * i"


# = int(input("введите ральную часть"))
#     = int(input("введите мимую часть"))
z1 = ComplexNum(2, 5)
z2 = ComplexNum(4, 8)
print(z1 + z2)
print(z1 * z2)