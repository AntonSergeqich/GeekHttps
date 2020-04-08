# 1.Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


write_list = []
while True:
    e = input("Введите данные, с 'Пробела начинать нельзя' (Для окончания нажмите Enter): ")
    if e == "":
        break
    elif e.startswith(" "):
        print("Я же говорил! Все сломалось, начинаем заново...")
        exit()
    else:
        write_list.append(e + "\n")


with open("ls5dz1_2.txt", "w", encoding="utf-8") as dz1_2:
    dz1_2.writelines(write_list)

num = 1
with open("ls5dz1_2.txt", encoding="utf-8") as dz1_2:
    for el in dz1_2.readlines():
        word = 1
        ind = 0
        for i in el:
            ind += 1
            if i == " ":
                if i == el[ind]:
                    pass
                else:
                    word += 1

        print(f"Строка - {num}: Слов в строке - {word}: {el[:len(el) - 1]}")
        num += 1
