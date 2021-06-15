#1
from time import sleep


class TrafficLight:
    color_1 = 'red'
    color_2 = 'yellow'
    color_3 = 'green'

    def running(self):
        print(color_1)
        sleep(7)
        print(color_2)
        sleep(2)
        print(color_3)


a = TrafficLight()
a.running()


#2
class Road:

    def __init__(self, l, w, t, m):
        self._length = l
        self._width = w
        self._thickness = t
        self._mass_1 = m

    def mass(self):
        self._thickness = self._thickness / 100 # в одном метре 100 см
        result = self._width * self._length * self._mass_1 * self._thickness
        print(result / 1000) # в одной тонне 1000 кг


r = Road(20, 5000, 25, 5)
r.mass()

#3
class Worker:

    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        result = sum(self._income.values())
        print(f'Total income: {result}')


p = Position('Ivan', 'Petrov', 'Developer', 100000, 20000)
p.get_full_name()
p.get_total_income()


#4
class Car:

    def __init__(self, s, c, n, i):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i

    def go(self):
        print(f"Go! {self.name}")

    def stop(self):
        print(f"Stop!")

    def turn(self):
        print("Turn")

    def show_speed(self):
        print(f'{self.name} moves with speed {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Speed limit exceeded! Slow down!")
        else:
            print(f'Moves with speed: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speed limit exceeded! Slow down!")
        else:
            print(f'Moves with speed:: {self.speed}')


class PoliceCar(Car):

    def go(self):
        print(f"Go! {self.is_police} {self.name}")


t = TownCar(60, 'green', 'BMW 7', False)
t.go()
t.turn()
t.show_speed()
t.stop()

print('---------------------')
s = SportCar(120, 'black', 'BMW M5 Competition', False)
s.go()
s.show_speed()
s.turn()
s.stop()

print('---------------------')
w = WorkCar(45, 'yellow', 'BMW 6 GT', False)
w.go()
w.show_speed()
w.turn()
w.stop()

print('---------------------')
p = PoliceCar(100, 'white - blue', 'Ford Focus', "PoliceCar")
p.go()
p.show_speed()
p.turn()
p.stop()


#5
class Stationery:

    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки с помощью ручки.')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки с помощью карандаша.')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки с помощью маркера')


s = Stationery('Пренадлежность')
s.draw()

print('---------------------------------------------------------')
p = Pen('Ручка')
p.draw()

print('---------------------------------------------------------')
pencil = Pencil('Карандаш')
pencil.draw()

print('---------------------------------------------------------')
h = Handle('Маркер')
h.draw()



