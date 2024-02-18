# https://graphviz.readthedocs.io/en/stable/manual.html
# у xdot есть свой питоновски модуль

# пердыдущие варианты реализации
# 1) из файл json. Разделение на пары из аходного предложения.
# 2) из объектов knowledge_base. Использование множества как структуры данных.
#  Подпись в каждой ноде какой класс и объект.



class Drawer():
    def __init__(self):
        self.path_local_dot = "knowledge_base/graphs_links/local_graph.dot"

    # здесь так же может быть код открытия в визуализаторе


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
                for node in link: # нельзя вязть и просто перебрать элементы т к в множестве так нельзя)
                    if node.__class__.__name__ == "_Object":

                        number = node.id

                        f.write('"' + node.name + "\n" + node.__class__.__name__ + " " + str(number) + '"')
                    else:
                        f.write('"' + node.name + "\n" + node.__class__.__name__ + '"')
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

    # еще необходим функционал режима отображения связей с классом и отсутвия отображения этих связей
    # продумать различные тесты с повотряющимися нодами и т п
    # добавить режим отображения id объектов

    def graph_to_xdot(self, graph):

        with open(self.path_local_dot, 'w') as f:
            f.write("strict graph G {\n")

            for link in graph.links:
                f.write('"' + str(link.one_node) + '" -- "' + str(link.two_node) + '"\n')

            f.write("}\n")
