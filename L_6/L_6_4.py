class Car:
    speed = float
    color = ""
    name = ""
    is_police = False
    _currentspeed = 0

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


    def go(self):
        self._currentspeed = self.speed


    def stop(self):
        self._currentspeed = 0


    def turn(self):
        if self._currentspeed == self.speed:
            print(f"поворот {self.color} {self.name}")
        else:
            print(f"стоп {self.color}  {self.name}")


    def show_speed(self):
        if self._currentspeed > 0:
            print(f"текущая скорость {self.color}  {self.name} {self.speed} км/ч")
        else:
            print(f"стоп {self.color} {self.name}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self._currentspeed > 60:
            print('превышение')
        else:
            print(f"текущая скорость {self.color} {self.name} {self._currentspeed}")


class SportCar(Car):
   '''спортивная машина '''


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):

        if self._currentspeed > 40:
            print(f'превышение {self.color} {self.name}')
        else:
            print(f"текущая скорость {self.color} {self.name} {self._currentspeed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def show_speed(self):
        if self.is_police:
            print("\033[31m{}\033[0m".format("полицейская машина"))


tc_speed = float(input("speed for town car"))
sc_speed = float(input("speed for spot car"))
wc_speed = float(input("speed for work car"))
pc_speed = float(input("speed for police car"))

tc = [
        TownCar(tc_speed, "red", "car1"),
        SportCar(sc_speed, "white", "car2"),
        WorkCar(wc_speed, "black", "car3"),
        PoliceCar(pc_speed, 'blue', 'police car')
    ]
for car in tc:
    car.show_speed()
for car in tc:
    car.go()
for car in tc:
    car.show_speed()
for car in tc:
    car.turn()
for car in tc:
    car.stop()
for car in tc:
    car.show_speed()



