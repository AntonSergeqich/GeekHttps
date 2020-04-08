# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def sliser(s):
    slice_list = []
    ind = 0
    buf = ' '

    n = str(s[s.index(" "):])
    n = n.replace("-", " ")
    n = n.replace("(пр)", " ")
    n = n.replace("(лаб)", " ")
    n = n.replace('(л)', ' ')
    n = n.replace('\n', ' ')

    for el in n:
        ind += 1
        if el == " ":
            pass
        elif el != ' ':
            buf = buf + el
            if n[ind] == ' ':
                slice_list.append(int(buf))
                buf = ' '
    return slice_list


les_list = []
hour_list = []
buf_list = []

with open('text_6.txt', encoding='utf8') as list_ls:
    for el in list_ls.readlines():
        ls = str(el[:el.index(":")])
        les_list.append(ls)
    list_ls.seek(0)
    for i in list_ls.readlines():
        buf_list.append(sliser(i))
    list_ls.seek(0)
    print(list_ls.read())

result_dict = {k: sum(buf_list[les_list.index(k)]) for k in les_list}
print(f"\n{result_dict}")
