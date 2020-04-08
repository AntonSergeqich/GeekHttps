# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from random import randint


color = ['\033[31mКрасного\033[0m', '\033[32mЗеленого\033[0m',
         '\033[33mЖелтого\033[0m', '\033[34mСинего\033[0m', '\033[36mБирюзового\033[0m']
name = ['\033[1mNissan\033[0m', '\033[1mMercedes\033[0m', '\033[1mGeely\033[0m',
        '\033[1mBMV\033[0m', '\033[1mVolvo\033[0m', '\033[1mKIA\033[0m']
turn = ['на лево', 'на право']


class Car:

    def __init__(self, car_speed, car_color, car_name, car_is_police, car_turn):
        self.car_speed = car_speed
        self.car_color = car_color
        self.car_name = car_name
        self.car_is_police = car_is_police
        self.car_turn = car_turn

    def go(self):
        print('Едем вперед')

    def stop(self):
        print('Приехали')

    def turn(self,):
        print(f"Поворачиваем {self.car_turn[randint(0, len(turn) - 1)]}")

    def show_speed(self):
        print(f'Едем со скоростью {self.car_speed}км ч.')


class Town_car(Car):
    def show_speed(self):
        print(f"Это городская машина едет со скоростью {self.car_speed}км ч.")
        if self.car_speed > 60:
            print(f'{self.car_speed}км ч. Очень быстро, помедленей.')


class Work_car(Car):
    def show_speed(self):
        print(f"Это рабочая машина едет со скоростью {self.car_speed}км ч. ")
        if self.car_speed > 40:
            print(f'Воу воу! Это же рабочий автомобиль. Не торопись.')


class Poliss(Car):
    def wiuwiu(self):
        print("Ого! Да мы полиция!")
        if self.car_is_police is True:
            print("\033[1mВИУ!!! ВИУ!!! ВИУ!!!\033[0m")


class SportCar(Car):
    def vrum(self):
        print("Я убер спортивная машиа ВРУМ ВРУМ!")
    def show_speed(self):
        print(f"\033[4mНесется со скоростью!! {self.car_speed}км ч.\033[0m")


print("Начинаем наше путешествие!")
auto_1 = Town_car(randint(10, 100), color[randint(0, len(color) - 1)], name[randint(0, len(name) - 1)], False,
                  turn)
print(f'\nАвтомобиль №1 {auto_1.car_color} цвета, марки "{auto_1.car_name}", начал движение')
auto_1.go()
auto_1.show_speed()
auto_1.turn()
auto_1.go()
auto_1.turn()
auto_1.stop()

auto_2 = Work_car(randint(10, 100), color[randint(0, len(color) - 1)], name[randint(0, len(name) - 1)], False,
                  turn)
print(f'\nАвтомобиль №2 {auto_2.car_color} цвета, марки "{auto_2.car_name}", начал движение')
auto_2.go()
auto_2.show_speed()
auto_2.go()
auto_2.turn()
auto_2.turn()
auto_2.turn()
auto_2.stop()

auto_3 = Poliss(randint(10, 100), color[randint(0, len(color) - 1)], name[randint(0, len(name) - 1)], True,
                  turn)
print(f'\nАвтомобиль №3 {auto_3.car_color} цвета, марки "{auto_3.car_name}", начал движение')
auto_3.go()
auto_3.wiuwiu()
auto_3.show_speed()
auto_3.go()
auto_3.turn()
auto_3.stop()

auto_4 = SportCar(200, color[randint(0, len(color) - 1)], name[randint(0, len(name) - 1)], True,
                  turn)
print(f'\nАвтомобиль №4 {auto_4.car_color} цвета, марки "{auto_4.car_name}", начал движение')
auto_4.go()
auto_4.vrum()
auto_4.show_speed()
auto_4.go()
auto_4.turn()
auto_4.stop()
