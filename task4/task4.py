import sys

if len(sys.argv) != 2:  # печатаем сообщение в случае не корректного заполнения
    print('Ошибка! Образец того как надо заполнить поле--->: python.py task4.py numbers.txt')
    sys.exit(1)     # выход из режима ввода

path_numbers_file = sys.argv[1]  # передаем аргумент в переменную


def minimal_move(p_n_f):  # функция выводящая минимальное количество ходов

    with open(p_n_f, 'r', encoding='utf-8') as file_list:  # открываю файл на чтение
        convert_to_lst = [int(digit) for digit in file_list.read().split()]     # конвертирую строку в список
        average_value = sorted(convert_to_lst)[len(convert_to_lst)//2]      # нахожу в отсортированном списке медиану
        result = sum(abs(digit - average_value) for digit in convert_to_lst)    # нахожу количество ходов
        return result


print(minimal_move(path_numbers_file))  # печатаю результат функции
