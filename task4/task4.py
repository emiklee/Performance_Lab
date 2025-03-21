import sys

with open('numbers.txt', 'w+', encoding='utf-8') as file:  # Создаем файл на запись входящих данных
    temp = ''   # переменная для сохранения данных
    for i in sys.stdin:     # открываю цикл для ввода данных
        temp += i.strip()+' '  # запись данных в переменную
    file.write(temp)  # запись файла

path_numbers_file = './numbers.txt'  # путь к созданному файлу


def minimal_move(p_n_f):  # функция выводящая минимальное количество ходов

    with open(p_n_f, 'r', encoding='utf-8') as file_list:  # открываю файл на чтение
        convert_to_lst = [int(digit) for digit in file_list.read().split()]     # конвертирую строку в список
        average_value = sorted(convert_to_lst)[len(convert_to_lst)//2]      # нахожу в отсортированном списке медиану
        result = sum(abs(digit - average_value) for digit in convert_to_lst)    # нахожу количество ходов
        return result


print(minimal_move(path_numbers_file))  # печатаю результат функции
