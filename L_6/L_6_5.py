class Stationery:

    title = ""
    line_type = ""

    def __init__(self, title, line_type):
        self.title = title
        self.line_type = line_type

    def draw(self):
        print(f"запуск отрисовки {self.title}\n выберите инструмент {self.line_type}")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title, "\033[1m{}\033[0m ")

    def draw(self):
        print(f"запуск отрисовки {self.title}\n выберите инструмент {self.line_type.format('карандаш')}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title, "\033[3m{}\033[0m")

    def draw(self):
        print(f"запуск отрисовки {self.title}\n выберите инструмент {self.line_type.format('ручка')}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title, "\033[4m{}\033[0m")

    def draw(self):
        print(self.line_type.format(f"запуск отрисовки {self.title}\n выберите инструмент"))


pen_title = "карандашный набросок"
pencil_title = "набросок ручкой"
handle_title = "рисунок фломастером"

draw_instrument = [Pen(pen_title),
                    Pencil(pencil_title),
                    Handle(handle_title)]

for instrument in draw_instrument:
    instrument.draw()



