from time import sleep
from random import randint

list_sunit = ["Принтер", "Сканер", "Копир"]
sklad_dict = {"Принтер": 0, "Сканер": 0, "Копир": 0}
sqad = ['Приемная', 'Архив', 'Бухгалтерия']


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class Pereferia:
    def __init__(self, format='A4', speed=20, color='Белый'):
        self.format = format
        self.speed = speed
        self.color = color


class Print(Pereferia):
    def __init__(self, cp="Цветная", format='A4', speed="20 стр. в мин", color='Белый'):
        super().__init__(format, speed, color)
        self.color_print = cp

    def __str__(self):
        return f"ПРИНТЕР\nОсновная характеристика: {self.color_print} печать\n" \
               f"Базовые характеристики: цвет устройства - {self.color}, формат печати - {self.format}," \
               f" скорость печати - {self.speed}"


class Scaner(Pereferia):
    def __init__(self, s="Сканирование", format='A4', speed="10", color='Белый'):
        super().__init__(format, speed, color)
        self.scan = s

    def __str__(self):
        return f"СКАНЕР\nОсновная характеристика: {self.scan}\n" \
               f"Базовые характеристики: цвет устройства - {self.color}, формат сканирования - {self.format}, " \
               f"скорость сканирования - {self.speed}"


class Copy(Pereferia):
    def __init__(self, copy="Копирование оригиналов", format='A3', speed="30", color='Белый'):
        super().__init__(format, speed, color)
        self.copy = copy

    def __str__(self):
        return f"КОПИР\nОсновная характеристика: {self.copy}\n" \
               f"Базовые характеристики: цвет устройства - {self.color}, формат сканирования - {self.format}, " \
               f"скорость сканирования - {self.speed}"


class Zakaz:
    def tabel(self):
        print("\033[1mЗаказ на поступление товара.\033[0m")
        for i, p in enumerate(list_sunit, 1):
            print(i, p)
        result = []
        print("Закрыть табель заказа - 0")
        k = input("Укажите позицию товара: ")
        if k == "0":
            return k
        c = input("Количество товара: ")
        result.append(k)
        result.append(c)
        return result


class Sklad:
    def __init__(self, k, c, chek=0, req=0):
        self.list_sunit = list_sunit
        self.count = c
        self.key = k
        self.sklad_dict = sklad_dict
        self.chek_out = chek
        self.req =req

    def unit_in(self):
        buf = self.sklad_dict[self.list_sunit[self.key - 1]] + self.count
        self.sklad_dict[list_sunit[self.key - 1]] = buf
        return f"{self.sklad_dict}"

    @property
    def request(self):
        self.req = randint(0, 2)
        print(f"\nЗапрос из отдела \033[4m{sqad[self.req]}\033[0m\n\033[4mПеречень техники на складе - "
              f"{self.sklad_dict}\033[0m")
        for i, p in enumerate(list_sunit, 1):
            print(i, p)
        while True:
            try:
                self.chek_out = int(input("Какое устройство будем отправлять? ")) - 1
                if self.chek_out > len(list_sunit) or self.chek_out < 0:
                    raise Error("\033[41mОШИБКА! Выбрана позиция вне списка!\033[0m")
                break
            except ValueError:
                print("\033[41mОШИБКА! Только цифры пожалуйста\033[0m")
            except Error as me:
                print(me)

        return self.chek_out

    @property
    def unit_out(self):
        if self.req == self.chek_out:
            print(f"\n\033[35m{self.list_sunit[self.chek_out]} уезжает в {sqad[self.req]}\033[0m")
            self.sklad_dict[list_sunit[self.chek_out]] -= 1
            for k, v in self.sklad_dict.items():
                if v <= 0:
                    print(f"\nОборудование \033[1m'{k}'\033[0m закончилось, необходимо дозаказать оборудование")
                    return 0
            return f"{self.sklad_dict}"
        else:
            return "\n\033[41mНеверный выбор, будьте внимательны!\033[0m"


print("ПО для тренировки снабженца!")
tab = Zakaz()
while True:
    result = tab.tabel()
    if result[0] == "0" or result[1] == "0":
        break
    try:
        sk_0 = int(result[0])
        sk_1 = int(result[1])
        if sk_0 > len(list_sunit) or sk_0 < 0:
            raise Error("\033[41mОШИБКА! Выбрана позиция вне списка!\033[0m")
        elif sk_1 < 0:
            raise Error("\033[41mОШИБКА! Мы принимаем, не отдаем!\033[0m")
        sk = Sklad(sk_0, sk_1)
        print(f"\033[4mПеречень техники на складе - {sk.unit_in()}\033[0m")
    except ValueError:
        print('\033[41mОШИБКА! Только цифры пожалуйста\033[0m')
    except Error as me:
        print(me)

p, s, c = Print(), Scaner(), Copy()
print(f"\033[1m{p}\033[0m")
sleep(2)
print(f"\033[1m{s}\033[0m")
sleep(2)
print(f"\033[1m{c}\033[0m")

print("\n\033[4mПравила отгрузки:\033[0m\n\033[31m1. В приемную устройство цветной печати\n2. В бухгалтерию устройство "
      "копирования\n3. В архив устройство сканирования\033[0m")

while True:
    zap = sk.request
    result = sk.unit_out
    if result == 0:
        ex = input("Надоело?\nДля выхода из программы наберите Выход, для продолжения Enter: ")
        if ex.lower() == 'выход':
            print("До скорых встреч!")
            exit()
        while True:
            result = tab.tabel()
            if result[0] == "0" or result[1] == "0":
                break
            try:
                sk_0 = int(result[0])
                sk_1 = int(result[1])
                if sk_0 > len(list_sunit) or sk_0 < 0:
                    raise Error("\033[41mОШИБКА! Выбрана позиция вне списка!\033[0m")
                elif sk_1 < 0:
                    raise Error("\033[41mОШИБКА! Мы принимаем, не отдаем!\033[0m")
                sk = Sklad(sk_0, sk_1)
                print(f"\033[4mПеречень техники на складе - {sk.unit_in()}\033[0m")
            except ValueError:
                print('\033[41mОШИБКА! Только цифры пожалуйста\033[0m')
            except Error as me:
                print(me)
