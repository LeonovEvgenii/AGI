"""."""
from scripts.classes.graph.Link import Link
from scripts.classes.graph.node.First_born import First_born
from scripts.classes.graph.node._Object import _Object


class Graph():
    """."""

    def __init__(self, name=''):
        """."""
        self.name = name

        self.classes = []
        self.objects = []

        # почему это список, а не множество ?
        self.nodes = []
        self.links = []

    # def add_node(self, node_obj):
    #     self.nodes.append(node_obj)

    def return_class(self, word):
        """Проверяет наличие класса."""
        for c_class in self.classes:
            if c_class.name == word:
                return c_class

        return False

    def add_node(self, word, number_in_sentence):
        """Добавляет вершину в граф."""
        new_object = None

        c_class = self.return_class(word)

        if c_class is False:

            new_class = First_born(word)
            self.classes.append(new_class)

            # Первый объект класса создается
            # и не в конструкторе класса, т к его еще вернуть обратно надо и
            # ссылку создать.
            # Операции над ссылками - это задача графа, а не класса _Class.
            # И так понятно, что все классы имеют связь со своими объектами.
            # А из конструктора класса возвращаться может только один объект и
            # это объект класса класс,
            # а не объект класса _Object.
            # Технически можно вернуть два объекта, но логически это
            # запутывает.
            new_object = _Object(new_class.name, number_in_sentence)
            new_class.add_obj(new_object)
            self.objects.append(new_object)

            self.add_link(new_class, new_object)

        else:
            # добавляем в объект

            # в параметры создания объекта передается только имя класса
            # сам _Object создается не внутри _Class, а снаружи
            # для добавления в список всех объектов в классе Graph.
            # Мог бы и внутри _Class создаваться, но тогда его возвращать надо
            # в Graph

            # это кстати идея
            # сделать автоматическое создание одного объекта при создании
            # класса
            # сделать метод возврата всех объектов
            # в классе граф при актуализации всех нод идет добавление класса и
            # вытаскивание из него всех объектов
            # раньше кстати так и было, создавался и класс и объект

            new_object = _Object(c_class.name, number_in_sentence)
            c_class.add_obj(new_object)
            self.objects.append(new_object)

            self.add_link(c_class, new_object)

        self.merge_list_nodes()

        return new_object

    def merge_list_nodes(self):
        """."""
        # можно изменить способ добавления объектов в общий список нод.
        # Бежим по спискам объектов каждого класса
        # и сначала добавляем класс, потом все объекты к нему относящиеся.
        self.nodes = self.classes + self.objects

    def add_link(self, old_node, new_node):
        """Добавляет связь между вершинами."""
        link = Link(old_node, new_node)
        self.links.append(link)

    def __str__(self) -> str:
        """Переопределение метода для печати графа в консоль."""
        print_nodes = ''
        for node in self.nodes:
            print_nodes += node.name + node.get_type()
            print_nodes += ' '

        print_links = ''
        for link in self.links:
            print_links += '\t' + str(link) + '\n'

        if print_nodes:
            return 'Граф:\n\t"' + self.name \
                + '"\nсписок вершин:\n\t' + print_nodes \
                + '\nсписок связей:\n' + print_links
        else:
            return 'граф пустой'

    # Удалял старые методы.
    # Я не знаю, зачем мне может понадобиться удалять все ссылки из графа,
    # но если, этот метод понадобится, он должен быть здесь.

    def clear(self):
        """Очистка всего графа."""
        # Важен ли порядок очистки ?
        # Можно ли очистив один список, не чистить другие ?
        self.classes.clear()
        self.objects.clear()
        self.nodes.clear()
        self.links.clear()
