# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


name_list = []
cash_list = []
f = 1
print("Список сотрудников и зряпплаты: ")
with open("text_3.txt", encoding="utf-8") as cash:
    for el in cash.readlines():
        s = float(el[el.index(" ") + 1:])
        u = str(el[:el.index(" ")])
        name_list.append(u)
        cash_list.append(s)
        print(f"{f}. {el[:-1].replace(' ', ' - ')} печенек.")
        f += 1
f = 1
print("\nСписок сотрудников с зряплатой меньше 20 000 печенек")
for el in cash_list:
    if el < 20000:
        print(f"{f} - {name_list[cash_list.index(el)]}")
        f += 1

print(f"\nРазмер зряплатного бюджета {sum(cash_list)} печенек.\nCредняя заряплата сотрудников "
      f"{sum(cash_list) / len(cash_list)} печенек")
