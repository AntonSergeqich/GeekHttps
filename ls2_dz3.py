# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Блок с исходными данными
moth_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
moth_dict = {1: "Январь - Зимний месяц", 2: "Февраль - Зимний месяц", 3: "Март - Весенний месяц",
             4: "Апрель - Весенний месяц", 5: "Май - Весенний месяц", 6: "Июнь - Летний месяц",
             7: "Июль - Летний месяц", 8: "Июнь - Летний месяц", 9: "Сентябрь - Осений месяц",
             10: "Октябрь - Осений месяц", 11: "Ноябрь - Осений месяц", 12: "Декабрь - Зимний месяц"}
# Ввод пользовательских данных
user_number = int(input("Укажите порядковый номер месяца (1 - 12): "))
# Защита от некоректоного ввода
while True:
    if user_number <= 0 or user_number > 12:
        print("Это некоректное число!")
        user_number = int(input("Укажите порядковый номер месяца (1 - 12): "))
    else:
        break
# Вывод данных
print(f"Время года: {moth_list[user_number - 1]}")
print(f"Это - {moth_dict.get(user_number)}")
