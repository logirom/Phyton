class Date:
    def __init__(self, date):
        day, month, year = Date.parseStr(date)
        if Date.validate(day, month, year):
            self.day = day
            self.month = month
            self.year = year
        else:
            raise ValueError("String is incorrect format")


    @classmethod
    def parseStr(cls, dateStr):
        parts = dateStr.split("-")
        if len(parts) != 3:
            raise ValueError("Incorrect format")
        return int(parts[0]), int(parts[1]), int(parts[2])

    @staticmethod
    def validate(day, month, year):
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        return True;



date = Date("21-12-2211")
print(f"{date.day} {date.month} {date.year}")
