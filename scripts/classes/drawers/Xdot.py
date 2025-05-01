"""Работа с graphviz и xdot."""

# https://graphviz.readthedocs.io/en/stable/manual.html
# у xdot есть свой питоновский модуль

# предыдущие варианты реализации
# 1) из файла json. Разделение на пары из входного предложения.
# 2) из объектов knowledge_base. Использование множества как структуры данных.
#  Подпись в каждой ноде какой класс и объект.

from scripts.classes.drawers.Drawer import Drawer


class Xdot(Drawer):
    """Основной класс."""

    def __init__(self):
        """Конструктор."""
        # критика хранения данного места
        # база знаний - это хранилище графов, а не хранилище xdot
        # если xdot генерирует специфичные файлы, то и пусть хранятся рядом с
        # классом
        # название папки graphs_links не имеет ничего общего с ссылками уже
        self.path_local_dot = 'knowledge_base/graphs_links/local_graph.dot'

        self.path_local = 'dot.dot'

    # устаревший метод, скорее всего как и класс knowledge_base

    def print_to_xdot_local(self):

        # чистить dot пока не надо, т к при перезапуске он все равно перетирается
        # в гите я его почищу
        # необходимости в принудительной операции пока нет, но будет потом

        # Источником связей могут служить список или файл json
        # Приоритетный источник список

        with open(self.path_local_dot, 'w') as f:
            f.write("strict graph G {\n")

            for link in self.kb.local_links:
                flag_two = False
                for node in link:  # нельзя вязть и просто перебрать элементы т к в множестве так нельзя)
                    if node.__class__.__name__ == "_Object":

                        number = node.id

                        f.write('"' + node.name + "\n" +
                                node.__class__.__name__ + " " + str(number) + '"')
                    else:
                        f.write('"' + node.name + "\n" +
                                node.__class__.__name__ + '"')
                    if flag_two:
                        break
                    else:
                        f.write(' -- ')
                        flag_two = True

                f.write('\n')

            f.write("}\n")

    def clear_local_dot(self):
        with open(self.path_local_dot, 'w') as f:
            f.write("strict graph G {\n")
            f.write("}\n")
        f.close()

    # продумать различные тесты с повторяющимися нодами и т п
    # добавить режим отображения id объектов

    def draw(self, graphs, mode='cls'):
        """Основной метод отрисовки."""
        with open(self.path_local, 'w') as f:
            f.write('strict graph G {\n')

            for graph in graphs:

                for link in graph.links:

                    # Предполагаемые режимы рисования:
                    # Сразу отметаю отображение только нод.
                    # их можно посмотреть в виде списка в консоли.
                    # Так же, они неудобно визуализируются graphviz без
                    # связей (в строчку).
                    # Поэтому интересно отображение только связей.
                    # Режим только объекты.
                    # Режим тех же объектов, но еще классы им принадлежащие.
                    # Больше комбинаций быть не может.
                    # Вывод одного определения или нескольких должен решаться
                    # правилами формирования ответа
                    # и может быть отрисован с помощью режима с классами.
                    # Не думаю, что будут определения целиком из классов.

                    if mode == 'obj':
                        if (link.one_node.get_type() == '_cls'
                                or link.two_node.get_type() == '_cls'):
                            continue

                    # проверку сделать, если нет связей

                    link_str = '"'

                    link_str += str(link.one_node)

                    if link.one_node.get_type() == '_obj':
                        link_str += ' id: '
                        link_str += str(link.one_node.id)

                    link_str += '" -- "'

                    link_str += str(link.two_node)

                    if link.two_node.get_type() == '_obj':
                        link_str += ' id: '
                        link_str += str(link.two_node.id)

                    link_str += '"\n'

                    f.write(link_str)

                    # f.write('"' + str(link.one_node) + '" -- "' + str(link.two_node) + '"\n')

            f.write('}\n')
