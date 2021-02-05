class Road:
    _lenght = 0
    _wight = 0


    def __init__(self, lenght, wight):
            self._lenght = lenght
            self._wight = wight

    def mass(self, mass_k, thickness ):
        mass = self._lenght * self._wight * mass_k * thickness/1000
        return mass

lenght = int(input("длина покрытия м "))
wight = int(input("ширина порытия м "))

new_r = Road(lenght, wight)
mass_k = int(input(f"коэффициент кг "))
thickness = int(input("толщина покрытия м "))
mass_result = new_r.mass(mass_k, thickness)
print(f"масса асфальта т {mass_result }")
