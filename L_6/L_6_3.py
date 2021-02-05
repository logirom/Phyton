class Woker:
    name = ""
    surname = ""
    position = ""
    _income = {}
    def __init__(self, n, sn, pst):
        self.name = n
        self.surname = sn
        self.position = pst
    def update_income(self, w, b):
        self._income["wage"] = w
        self._income["bonus"] = b


class Position(Woker):
    def __init__(self, n, sn, pst):
        super().__init__(n, sn, pst)

    def get_full_name(self):
       return f"{self.name} {self.surname}"

    def get_total_income(self):
        income_wb = self._income["wage"]*12+self._income["bonus"]
        return income_wb
new_w = Position("Ivan", "Petrov", "dvornik")
new_w.update_income(199, 99)
print(new_w.get_full_name(), new_w.get_total_income())
