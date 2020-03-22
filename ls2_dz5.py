# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.


# Блок исходных данных
my_list = [7, 5, 3, 3, 2]
print(my_list)
# Ввод данных
user_reit = int(input("Рейтинг: "))
# Глобальная переменная
maximum_list = 0
# Блок вычесления максимального значения в списке
for i in my_list:
    if i > maximum_list:
        maximum_list = i
# Блок внесения информации в рейтинг
if user_reit in my_list:    # Проверка наличия значения в списке
    my_list_index = my_list.index(user_reit)
    my_list.insert(my_list_index, user_reit)
elif maximum_list < user_reit:  # Проверка на максимальное значение в рейтинге
    my_list.insert(0, user_reit)
else:
    my_list.append(user_reit)
# Вывод информации
print(my_list)
