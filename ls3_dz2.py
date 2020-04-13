# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
"""
К сожалению не совсем уловил понятие "именнованые аргументы" Я воспринял их как "любое количество".
Кажется второй вариант соостветствует условиям задачи. Если не прав прошу разъяснить.
"""
anket = ['Ваше имя: ', 'Ваша фамилия: ', 'Год рождения: ', 'Город проживания: ', 'e-mail: ', 'Ваш телефон: ']
result = []

"""
Вариант 1: Статичные аргументы
"""
def base_les (name, sec_name, years, town, mail, tel):
    print(f"Имя - {name}  Фамилия - {sec_name}  Год рождения - {years} Город проживания - {town} e-mail - {mail} "
          f"телефон - {tel}")

"""
Вариант 2: Именные аргументы
"""
def base_list (*args):
    print("ВЫВОД ДАННЫХ ПО СПИСКУ:")
    for i in args:
        print(" ".join(i))

"""
Вариант 3: Списочный
"""
def base_dict (**kwargs):
    print("ВЫВОД ДАННЫХ ПО СЛОВАРЮ:")
    for i in kwargs.items():
        print(": ".join(i))

base_les(input("Имя: "), input("Фамилия: "), input("Год рождения: "), input("Город проживания: "),
               input("e-mail: "), input("Телефон: "))

for i in anket:     # Заполняем список для отправки в функцию
    result.append(input(f"{i}"))

base_list(result)
base_dict(Имя=result[0], Фамииля=result[1], Год=result[2], Город=result[3], Email=result[4], Телефон=result[5])

