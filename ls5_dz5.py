# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


while True:
    my_list = []
    result_list = []
    while True:
        try:
            n = (int(input('Введите числа. (Для начала сложения вводим "0"): ')))
            if n == 0:
                break
            my_list.append(str(n) + " ")
            print(f'Будем складывать: {"+ ".join(my_list)}')
        except ValueError:
            print('Вводим только цифры!')

    with open('number_sum.txt', 'w', encoding='utf-8') as number_enter:
        number_enter.writelines(my_list)

    with open('number_sum.txt', encoding='utf-8') as number_sum:
        i = ""
        for el in number_sum.readline():
            if el != " ":
                i = i + el
            else:
                result_list.append(int(i))
                i = ""
        print(f'\nСумма чисел = {sum(result_list)}')

    restart_program = input("\n(0 - Нет 1 - Да) Еще раз? ")
    while True:
        if restart_program == "0":
            print('До новых встреч!')
            exit()
        elif restart_program == "1":
            break
        else:
            print(f"Ошибка, не могу распознать команду: {restart_program}")
            restart_program = input("(0 - Нет 1 - Да) Еще раз? ")
