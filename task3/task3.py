import json
import sys

if len(sys.argv) != 4:  # печатаем сообщение в случае не корректного заполнения
    print('Ошибка! Образец того как надо заполнить поле--->: python.py task3.py values.json tests.json report.json')
    sys.exit(1)     # выход из режима ввода

path_values = sys.argv[1]   # передаем 1 аргумент в переменную
path_tests = sys.argv[2]    # передаем 2 аргумент в переменную
path_report = sys.argv[3]   # передаем 3 аргумент в переменную


def extract_value(obj, key, val, m_d):  # рекурсивная функция для распаковки values.json
    if isinstance(obj, dict):  # проверка на тип данных - словарь
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                extract_value(v, key, val, m_d)
            else:
                m_d[obj[key]] = obj[val]

    elif isinstance(obj, list):  # проверка на тип данных - список
        for item in obj:
            extract_value(item, key, val, m_d)

    return m_d


def insert_tests(obj, key, val, m_d):  # рекурсивная функция для распаковки values.json
    if isinstance(obj, dict):  # проверка на тип данных - словарь
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                insert_tests(v, key, val, m_d)
            else:
                if val in obj:
                    obj[val] = m_d[obj[key]]
                else:
                    continue
    elif isinstance(obj, list):  # проверка на тип данных - список
        for item in obj:
            insert_tests(item, key, val, m_d)

    return obj


def report(v, t, r):  # главная функция которая записывает данные в файл report.json
    key = 'id'  # переменная с ключом для передачи в рекурсивной функции
    val = 'value'  # переменная с ключом для передачи в рекурсивной функции
    my_dict = dict()  # создаем словарь для наполнения данными полученными из файла values.json

    with (open(v, 'r', encoding='utf-8') as value_file,  # открываю файлы на чтение/чтение/запись
          open(t, 'r', encoding='utf-8') as test_file,
          open(r, 'w+', encoding='utf-8') as report_file):
        result_v = json.loads(value_file.read())  # считываю данные value_file в переменную

        result_t = json.loads(test_file.read())  # считываю данные test_file в переменную

        resul_extract_value = extract_value(result_v, key, val, my_dict)  # вызываю рекурсивную функцию для result_v

        resul_insert_tests = insert_tests(result_t, key, val, my_dict)  # вызываю рекурсивную функцию для result_t

        json.dump(resul_insert_tests, report_file, indent=2)  # записываю результат в report_file

        return resul_insert_tests  # возвращаю результат


report(path_values, path_tests, path_report)  # вызываю функцию
