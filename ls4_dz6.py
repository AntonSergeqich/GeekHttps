# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
from itertools import count, cycle

"""
Не уверен что почестному использовать "exit" :) но другого в голову ничего не пришло.
"""

my_list = []
cyc_list = []
for i in count(1):
    my_list.append(i)
    if len(my_list) == 20:
        print(f"Модуль count - {my_list}")
        for n in cycle(my_list):
            cyc_list.append(n)
            if len(cyc_list) == 50:
                print(f"Модуль cycle - {cyc_list}")
                exit()
