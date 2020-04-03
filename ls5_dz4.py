# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


eng_list = ['One', 'Two', 'Three', 'Four']
rus_list = ['Один', 'Два', 'Три', 'Четыре']
result_list = []
e = 0
r = 0
with open('text_4.txt', encoding='utf-8') as number:
    print('Выгруженный из файла список:')
    for el in number.readlines():
        print(el.replace('\n', ""))
        result_list.append(el.replace(eng_list[e], rus_list[r]))
        e, r = e + 1, r + 1
print(f'\nЗаписываемый блок в файл: {result_list}')

with open('text4_rus.txt', 'w', encoding='utf-8') as rus_number:
    rus_number.writelines(result_list)

with open('text4_rus.txt', 'r', encoding='utf-8') as rus_number:
    print(f'\nТестовая выгрузка из нового файла:\n{rus_number.read()}')
