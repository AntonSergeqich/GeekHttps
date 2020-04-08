# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income_z, income_w):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {income_z: 0, income_w: 0}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя: \033[1m{self.name}\n\033[0mФамилия: \033[1m{self.surname}')

    def get_full_income(self):
        print(f'\033[0mДоход (с учетом премии): \033[1m{sum(self._income)}\033[0m печенек.')


work_data = Position('User', 'UseroFF', 'Program meneger', 100, 1000)
work_data.get_full_name()
work_data.get_full_income()
