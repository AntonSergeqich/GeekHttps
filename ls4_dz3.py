# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


def print_number(number):
    if number == 0:
        print("До скорых встреч!")
        exit()
    else:
        result_all = [el for el in range(20, 240) if el % number == 0]
        return result_all


result_21 = [el for el in range(20, 240) if el % 21 == 0]
result_20 = [el for el in range(20, 240) if el % 20 == 0]

print(f"Ищем кратное! Вводите число, мы ищем кратное в диапазоне от 20 до 240\nНапример 20 - {result_20}\n"
      f"или 21 - {result_21}")

while True:
    print(print_number(int(input("Попробуйте сами! (Для выхода наберите 0): "))))
