# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на
# экран. Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class OwnError(Exception):
    def __init__(self, bag):
        self.bag = bag

    def __str__(self):
        return self.bag


result_list = []
while True:
    try:
        user_number = int(input('Введите число для добавления в список: '))
        if user_number < 0:
            raise OwnError("Только положительные! Эмоции и числа!")
    except ValueError:
        print("Неа, добавляем только числа, еще раз.")
    except OwnError as err:
        print(err)
    else:
        print(f"Добавляем: {user_number}")
        result_list.append(user_number)
        ex = input('Надоело?\nНабери \033[1m"Выход"\033[0m, "Enter" для продолжения: ')
        if ex.lower() == "выход":
            print(f"Ваш список - {result_list}\nВсего хорошего!")
            break