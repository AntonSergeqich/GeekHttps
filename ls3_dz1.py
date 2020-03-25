# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division (a, b):
    try:
        a, b = int(a), int(b)
        r = a / b
        r = round(r, 2)
        return r
    except ZeroDivisionError:
        print('Мы не делим на "0", будьте внимательны.')
    except ValueError:
        print("Неверный символ, будьте внимательны.")
result = None
while result == None:
    print("Деление А на Б")
    result = division(input('Введите число "A": '), input('Введите число "Б": '))

print(f"Результат - {result}")
