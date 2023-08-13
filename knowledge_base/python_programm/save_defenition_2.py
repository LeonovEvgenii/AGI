# сохрани_определение 1 2 3

import sys

# from ...scripts.classes.Knowledge_base import Knowledge_base
# Относительный импорт не работает из за ошибки:
# attempted relative import with no known parent package
# Решения:
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# Попробовать оформить проект как package или с __init__.py
# и уже там автоматически сообщать абсолютный путь автоматически.
# Возможно subprocess это не касается 
# и придется путь передавать в subprocess параметром. 
# Пока термение закончилось и в subprocess сделаю абсолютный импорт.

sys.path.append("/home/evgeniy/git/AGI/scripts/classes")
# комментарий NOQA нужен для autopep8, чтоб не перемещатлась стока выше sys.path.append()
from Knowledge_base import Knowledge_base  # NOQA


kb = Knowledge_base()

# kb.create_def(sys.argv[2], sys.argv[3:])


# функция БЗ чтение класса


params = sys.argv[2:]

if len(params) > 1:
    if params[0][-3:] != ".py":
        if len(params) == 2 and params[1][-3:] == ".py":
            print("первород")
            exit(0)
        for param in params:
            if param [-3:] == ".py":
                print("ошибка")
                exit(0)
        print("вторород")
    else:
        print("ошибка")
else:
    print("ошибка")
    # обработать ошибку в core

# если больше 1
#     если первый не ру
#         если их два и второ ру
#             открыть класс
#             сохр первор
#         если их больше двух и нет ру
#             открыть класс
#             сохр втор
#     иначе ошибка
# иначе ошибка



# как работает флаг "необходимость_дальнейшего_выполнения"
# когда потом срабатывает отрисовка


# определения собираются из нод классов
# создание связей слова которое определяется с каждым словом входящим в его состав
# зписать в ТЗ о создании автоматичексих тестов всех фалов программы

