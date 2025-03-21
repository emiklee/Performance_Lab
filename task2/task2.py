from math import sqrt

path_circle = './circle.txt'  # путь к файлу с координатами центра окружности и его радиусом.
path_dot = './dot.txt'  # путь к файлу с координатами точек.


def find_dot(x, y, z):  # Функция, которая получает на вход координаты центра окружности/радиус/координаты точек
    # и на выходе мы получаем положение точки относительно окружности

    circle_coordinate_1, circle_coordinate_2 = x.split()  # разбиваем на переменные координаты центра окружности
    dot_coordinate_1, dot_coordinate_2 = z.split()  # разбиваем на переменные координаты точек

    result = sqrt(((int(dot_coordinate_1) - int(circle_coordinate_1)) ** 2 +  # расчет по формуле
                   (int(dot_coordinate_2) - int(circle_coordinate_2)) ** 2))

    if result < sqrt(int(y) ** 2):  # если корень числа меньше чем корень радиуса, то точка внутри
        return '1'
    elif result == sqrt(int(y) ** 2):  # если корни числа равны, то точка на окружности
        return '0'
    else:
        return '2'  # если корень числа больше чем корень радиуса, то точка снаружи


def circle(p_c, p_d):  # Главная функция
    result = ''  # Переменная для записи результатов

    # Открываем файлы на чтение
    with open(p_c, 'r', encoding='utf-8') as file_pc, open(p_d, 'r', encoding='utf-8') as file_pd:
        circle_center, circle_radius = file_pc.readlines()
        circle_dot = file_pd.readlines()

        for i in circle_dot:  # Перебираем наши координаты точек

            # вызываем функцию и записываем результат функции в переменную
            result += find_dot(circle_center, circle_radius, i) + '\n'

    return result  # Возвращаем общий результат


print(circle(path_circle, path_dot))  # Вызываем главную функцию и передаем аргументы
