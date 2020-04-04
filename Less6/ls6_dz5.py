# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, name):
        self.name = name


    def draw(self):
        print(f'Запускаем отрисовку:')

class Pen(Stationery):
    def draw(self):
        print(f'Запускаем отрисовку: \033[3m\033[34m{self.name}\033[0m')

class Pencil(Stationery):
    def draw(self):
        print(f'Запускаем отрисовку: \033[2m{self.name}\033[0m')

class Handle(Stationery):
    def draw(self):
        print(f'Запускаем отрисовку: \033[1m\033[35m{self.name}\033[0m')


Pen('Ручкой').draw()
Pencil('Карандашем').draw()
Handle('Маркером').draw()
