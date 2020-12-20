# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class Comp_Number:
    def __init__(self, num):
        self.num = num

    def converse(self):
        result = []
        buf = ''
        for el in self.num:
            if el == '+' or el == 'i':
                result.append(int(buf))
                buf = ''
            else:
                buf += el
        return result

    def __add__(self, other):
        w = len(self.num)
        i = 0
        r = []
        while w != 0:
            buf = self.num[i] + other.num[i]
            r.append(str(buf))
            w, i = w - 1, i + 1
        return f"{'+'.join(r)}i"

    def __mul__(self, other):
        w = len(self.num)
        i = 0
        r = []
        while w != 0:
            buf = self.num[i] * other.num[i]
            r.append(buf)
            w, i = w - 1, i + 1
        return r


while True:
    try:
        num_1 = input("Пример (A+Bi)\nВведите ПЕРВОЕ комплексное число: ")
        num_2 = input("Пример (A+Bi)\nВведите ВТОРОЕ комплексное число: ")
        if '+' not in num_1 or '+' not in num_2:
            raise Error("ОШИБКА! Отсутствует знак '+'! Ввод согласно шаблону! - (A+Bi)")
        elif 'i' not in num_1 or 'i' not in num_2:
            raise Error("ОШИБКА! Отсутствует знак 'i'! Ввод согласно шаблону! - (A+Bi)")
        else:
            break
    except ValueError:
        print("Ввод согласно шаблону! - (A+Bi)")
    except Error as me:
        print(me)

"""Сложение"""
user_num_1 = Comp_Number(num_1)
user_num_2 = Comp_Number(num_2)
list_num_1 = user_num_1.converse()
list_num_2 = user_num_2.converse()
summ_num_1 = Comp_Number(list_num_1)
summ_num_2 = Comp_Number(list_num_2)
print(f"\nСкаладываем: {num_1} и {num_2}\nПолучаем - {summ_num_1 + summ_num_2}")

"""Умножение"""
mul_num_1 = Comp_Number(list_num_1)
mul_num_2 = Comp_Number(list_num_2)
result_m1 = (mul_num_1 * mul_num_2)
mul_part_1 = result_m1[0] - result_m1[1]
mul_num_1 = Comp_Number(list_num_1[::-1])
result_m2 = (mul_num_1 * mul_num_2)
mul_part_2 = result_m2[0] + result_m2[1]
print(f"\nПеремножаем: {num_1} и {num_2}\nПолучаем - {mul_part_1}+{mul_part_2}i")
