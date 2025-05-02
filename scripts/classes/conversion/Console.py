"""."""

from scripts.classes.conversion.Converter import Converter
from scripts.classes.graph.Graph import Graph


class Console(Converter):
    """."""

    def __init__(self):
        """."""
        super().__init__()
        self.output_content = ''

    def content_to_graphs(self, text_raw):
        """."""
        checked_text = self.__check_for_emptiness(text_raw)

        formatted_text = self.__formatting(checked_text)

        list_sentences = self.__create_list_sentences(formatted_text)

        # проверку не вынести в __create_list_words т к здесь нужно решать:
        # если список пустой сразу вернуть граф
        # тип возвращаемого значения граф, даже если без нод
        if list_sentences:

            # принятое решение 23
            # все конвертеры работают с массивами графов.
            graphs = []

            for sentence in list_sentences:

                old_node = None
                graph = Graph()

                for i, word in enumerate(sentence):

                    new_node = graph.add_node(word, number_in_sentence=i + 1)

                    if old_node:
                        graph.add_link(old_node, new_node)

                    old_node = new_node

                graphs.append(graph)

        else:
            print('Входной контент не содержит ни одного ключевого слова')

        # Почему возвращается именно список графов, а не один
        # Аналитика между графами / предложениями производится в core, а не в
        # консоле.

        self.output_graphs = graphs

        return self.output_graphs

    def __check_for_emptiness(self, text):
        if text is None:
            while 1:
                input_str = input('Ввод: ')
                if input_str == '':
                    print('Введена пустая строка')
                    continue
                else:
                    break
            return input_str

        else:
            return text

    def __formatting(self, input_str) -> list:
        input_str = input_str.lower()

        punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
        for p in punctuation:
            if p in input_str:
                input_str = input_str.replace(p, '')

        return input_str

    def __create_list_sentences(self, input_str):

        input_list_sentences = input_str.split('.')

        # можно так же хранить номер предложения в тексте
        for number, sentence in enumerate(input_list_sentences):
            list_words = sentence.split(' ')
            list_words = [i for i in list_words if i]

            input_list_sentences[number] = list_words

        input_list_sentences = [i for i in input_list_sentences if i]

        return input_list_sentences

    def graphs_to_content(self, input_graphs):
        """."""
        # можно вызывать родительский метод с тем же названием
        # super().graphs_to_content()

        text = ''

        for input_graph in input_graphs:
            text += self.graph_to_text(input_graph)
            text += '. '

        text = text[:-1]

        self.output_content = text

        return text

    def graph_to_text(self, input_graph):
        """."""
        copy_links = input_graph.links.copy()

        sentence = []

        for link in copy_links:

            # Принятое решение #
            # Логика формирования строки отличается от класса drawer.
            # Drawer нужен для дебага, консоль нет.

            if (link.one_node.get_type() == '_cls'
                    or link.two_node.get_type() == '_cls'):
                continue

            if len(sentence) == 0:
                sentence.append(link.one_node)
                sentence.append(link.two_node)
                copy_links.remove(link)
                continue

            if link.one_node == sentence[-1]:
                sentence.append(link.two_node)
                copy_links.remove(link)
                continue

            if link.two_node == sentence[-1]:
                sentence.append(link.one_node)
                copy_links.remove(link)
                continue

        sentence_text = ''

        for obj_word in sentence:
            sentence_text += obj_word.name
            sentence_text += ' '

        # удаляю последний пробел
        sentence_text = sentence_text[:-1]

        return sentence_text
