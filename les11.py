# 1
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def int_method(cls, day, month, year):
        day = int(day)
        month = int(month)
        year = int(year)
        return (f"Дата: {day} day: {month} month : {year} year")

    @staticmethod
    def valid(day, month, year):
        if day <= 30 and month <= 12 and year <= 365:
            return (f"Дата: {day} day: {month} month : {year} year")
        else:
            return "err"


print(Date.int_method(1, 2, 3))
print(Date.valid(1, 2, 3))


#2
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите положительное число: ")

try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise OwnError("Вы ввели отрицательное число!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число {inp_data}")