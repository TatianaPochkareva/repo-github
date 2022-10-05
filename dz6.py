# # задача №1
from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print("Красный режим светофора")
        sleep(7)
        print("Желтый режим светофора")
        sleep(2)
        print("Зеленый режим светофора")
        sleep(10)

traf_light = TrafficLight()
traf_light.running()


# # задача №2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return (self._length * self._width * 25 * 0.05) / 1000

road1 = Road(5000, 20)
print('Масса асфальта: ', (road1.mass()), 'тонн')


# задача №3
class  Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Sergey', 'Petrov', 'manager', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# задача №4
class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn_right(self):
        print(f'машина {self.name} повернула направо')

    def turn_left(self):
        print(f'машина {self.name} повернула налево')

    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed}')

class Towncar(Car):
    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed}')
        if self.speed > 60:
            print(f'машина {self.name}  превысила допустимую скорость')
        else:
            print(f'машина {self.name} скорость не превысила')

class Workcar(Car):
    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed}')
        if self.speed > 40:
            print(f'машина {self.name}  превысила допустимую скорость')
        else:
            print(f'машина {self.name} скорость не превысила')

class Sportcar(Car):
    pass

class Policecar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = Towncar(90, 'White', 'Oka')
town_car.go
town_car.show_speed()

work_car = Workcar(35, 'Rose', 'Lada')
work_car.go
work_car.show_speed()

Police_car = Policecar(110, 'Blue',  'Ford', True)
Police_car.stop()
Police_car.show_speed()
print(Police_car.is_police)

sport_car = Sportcar(100, 'Red', 'Audi', False)


# задача №5
class Stationery:
    def __init__(self, title="Рисование"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f' Запуск отрисовки ручкой {self.title}')

class Pencil(Stationery):

    def draw(self):
        print(f" Запуск отрисовки карандашом {self.title}")

class Handle(Stationery):

    def draw(self):
        print(f" Запуск отрисовки маркером {self.title}")

st = Stationery ()
st.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()
