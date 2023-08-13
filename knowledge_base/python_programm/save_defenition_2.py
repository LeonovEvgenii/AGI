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

# первородные определения не сохраняются
# нет сообщения о том, что недостаточно количество параметров
# как работает флаг "необходимость_дальнейшего_выполнения"
# когда потом срабатывает отрисовка


# определения собираются из нод классов
# создание связей слова которое определяется с каждым словом входящим в его состав

