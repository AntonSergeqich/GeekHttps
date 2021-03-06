# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна Использовать формулу: длинаширинамасса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, _road_width, _road_lenght):
        self._road_lenght = _road_lenght
        self._road_width = _road_width
        print(f'Для реализации проекта по созданию новой дороги\n\033[1mШириной - {_road_width} метров.\n'
              f'Длинной - {_road_lenght} метров.\n\033[0mПонадобится: '
              f'{self._road_width * self._road_lenght * 25 * 5 / 1000} тонн асфальта.')


print('Делаем хорошие дороги!\n!!!Внимание, данная программа не учитывает откатов и иных бонусных программ!!!'
      ' Разработчик ответствености за недосчитанные деньги !!!НЕ НЕСЕТ!!!')
new_road = Road
try:
    new_road(int(input("Ширина дорожного полотна (ввод производится в мерах): ")),
             int(input("Длинна дорожного полотна (ввод производится в мерах): ")))
except ValueError:
    try:
        print("Метры пишутся измеряются в цифрах. Будьте внимательны!")
        new_road(int(input("Ширина дорожного полотна (ввод производится в мерах): ")),
                 int(input("Длинна дорожного полотна (ввод производится в мерах): ")))
    except ValueError:
        print("Видимо это программа не для Вас. Всего хорошего.")
        exit()
