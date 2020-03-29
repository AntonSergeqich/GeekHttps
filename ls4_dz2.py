# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
from random import randint


my_list = []
for i in range(10):
    my_list.append(randint(1, 300))

result_list = [el for el in my_list[1:] if el > my_list[my_list.index(el) - 1]]

print(f"Оригинальный список - {my_list}")
print(f"Результативный список - {result_list}")
