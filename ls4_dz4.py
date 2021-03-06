# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
from random import randint


my_list = []
for i in range(12):
    my_list.append(randint(1, 10))
print(f"Оригинальный список - {my_list}")

result_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Результативный список - {result_list}")
