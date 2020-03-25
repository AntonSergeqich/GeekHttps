# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
Реализовал оба варианта, плюс вариант деления на 1
"""


def my_func(x, y):
    global r
    if y == -1:
        print(1 / x)
    else:
        print(x ** y)
        i = abs(y)
        while i > 0:
            i -= 1
            r = (x * x)
        print(1 / r)


print('Возводим в отрицательную степень.')
x = int(input("Вводим первое, положительное число: "))
y = int(input("Вводим второе, отрицаельное число: "))

while x <= 0 or y >= 0:
    print('Неверный ввод, повторите попытку')
    x = int(input("Вводим первое, положительное число: "))
    y = int(input("Вводим второе, отрицаельное число: "))

my_func(x, y)
