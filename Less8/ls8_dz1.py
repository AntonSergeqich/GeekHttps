# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def number_data(cls, param):
        buf = ''
        result = []
        for el in param:
            if el != "-":
                buf += el
            if el == "-":
                result.append(int(buf))
                buf = ''
        result.append(int(buf))
        return result

    @staticmethod
    def find_data(chek):
        if chek[0] < 1 or chek[0] > 31:
            return f"\nОШИБКА! - {chek[0]} - Не календарное значение \033[4mдня\033[0m."
        elif chek[1] < 1 or chek[1] > 12:
            return f"\nОШИБКА! - {chek[1]} - Не календарное значение \033[4mмесяца\033[0m."
        elif chek[2] > 9999 or chek[2] < 0:
            return f"\nОШИБКА! - {chek[2]} год за пределами осмысления \033[4mкалендаря\033[0m."
        else:
            return "\nВведеная дата имеет календарный формат (ДД-ММ-ГГГГ)"

    def com(self):
        num_data = self.number_data(self.data)
        result = Data.find_data(num_data)
        print(result)
        return self.data


buf = ''
print("Введите дату 2-значным числом (ДД-ММ-ГГГГ)")
while True:
    try:
        my_data = [abs(int(input(f"Число: "))), abs(int(input(f"Месяц: "))), abs(int(input(f"Год: ")))]
        break
    except ValueError:
        print(f"Ошибочный ввод")
        print("Введите дату 2-значным числом (ДД-ММ-ГГГГ)")

buf = buf + str(my_data[0]) + "-" + str(my_data[1]) + "-" + str(my_data[2])
my_data = Data(buf)
print(my_data.com())
