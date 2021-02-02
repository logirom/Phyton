from time import sleep
class TrafficLight:
    __color = ""


    def run(self, n):
         states = [("red", 31,  7), ("yellow", 33, 2), ("green", 32, 5), ("yellow", 33, 2)]
         for i in range(n):
             for color, code, time in states:
                 self.__color = color
                 fstr = "\r\33[" + str(code) + "m {} "
                 print(fstr.format(self.__color), end = '')
                 sleep(time)
trl = TrafficLight()
trl.run(int(input("количество циклов ")))
