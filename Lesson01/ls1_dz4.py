#  Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.

number = int(input("Введите несколько цифр а мы угадаем какое самое большое: "))
result = 0

while number > 0:   # Цикл поиска наибольшего числа
    calc = number % 10
    if calc > result:
        result = calc
        number = number // 10
    else:
        number = number // 10

print(result)
