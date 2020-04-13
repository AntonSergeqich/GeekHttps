# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

total = -1
class Crafting(ABC):

    def __init__(self, total_cloth):
        self.total_cloth = total_cloth
        self.count_c = 0
        self.count_s = 0
        self.total_cloth_res = total_cloth

    @property
    def chek(self):
        if self.total_cloth < 0:
            print(f"У вас кончились ресурсы. Перерасход - {self.total_cloth:.2f}, занесите в следующий раз.")
            return False

    @property
    def suit(self):
        try:
            cloth = int(input("Ваш размер? "))
        except ValueError:
            return "Не тот размерчик, давайте еще раз."
        self.count_s += 1
        craft = 2 * cloth + 0.3
        self.total_cloth -= craft
        return f"Потрачено {craft}, осталось ткани {self.total_cloth:.2f}"

    @property
    def coat(self):
        try:
            cloth = int(input("Ваш рост? "))
        except ValueError:
            return "Не тот размерчик, давайте еще раз."
        self.count_c += 1
        craft = cloth/6.5 + 0.5
        self.total_cloth -= craft
        return f"Потрачено {craft}, осталось ткани {self.total_cloth:.2f}"

    @property
    def total(self):
        return f"Изготовлено:\n {self.count_s} - костюмов.\n {self.count_c} - пальто.\nПотрачено ткани: " \
               f"{self.total_cloth_res - self.total_cloth:.2f}\nПриходите еще!"


print('Ателье "Костюм Пальто Стеклопакет"')
while total < 0:
    try:
        total = (int(input('Каким колличеством ткани вы располагаете? ')))
    except ValueError:
        print("Только цифры")
total = Crafting(total)
while True:
    if total.chek == False:
        break
    craft = input('Мы можем сшить "Пальто" или "Костюм" для выхода нашмите "Enter"\n'
                  'Чего изволите? ')
    if craft.lower() == 'пальто':
        print(total.coat)
    elif craft.lower() == 'костюм':
        print(total.suit)
    elif craft.lower() == 'стеклопакет':
        print('Наш мастер свяжется с Вами')
    elif craft == "":
        break
    else:
        print("Мы этого шить не умеем")

print(total.total)
