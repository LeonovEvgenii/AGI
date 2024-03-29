from scripts.classes.Converter import Converter


class Console(Converter):

    output_content = ""

    def __init__(self):
        super().__init__()

    def content_to_graph(self, text=None):

        if text == None:
            while 1:
                input_str = input("Ввод: ")
                if input_str == "":
                    print("Введена пустая строка")
                    continue
                else:
                    break

        self.paste_input_data(text)

        return self.get_graph()

    def __formatting(self, input_str) -> list:
        input_str = input_str.lower()

        punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
        for p in punctuation:
            if p in input_str:
                input_str = input_str.replace(p, '')

        input_list_words = input_str.split(" ")
        
        input_list_words = [ i for i in input_list_words if i ]

        return input_list_words

    def paste_input_data(self, input_str):
        input_list_words = self.__formatting(input_str)

        if input_list_words:

            old_node = None
            
            for i, word in enumerate(input_list_words):

                new_node = self.output_graph.add_node(word, number_in_sentence = i + 1)

                if old_node:
                    self.output_graph.add_link(old_node, new_node)

                old_node = new_node
            
        else:
            print("Строка не содержит ни одного ключевого слова")

    def graph_to_content(self, input_graph, print_flag=False):
        # можно вызывать родительский метод с тем же названием
        # super().graph_to_content() 
        
        self.write_output_data(input_graph)
        
        if print_flag:
            print(self.get_content())

        return self.get_content()

    def write_output_data(self, input_graph):

        copy_links = input_graph.links.copy()

        sentence = []

        for link in copy_links:

            ### Принятое решение ###
            # Логика формирования строки отличается от класса drawer.
            # Drawer нужен для дебага, консоль нет.

            if link.one_node.get_type() == "_cls" or link.two_node.get_type() == "_cls":
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


        for obj_word in sentence:
            self.output_content += obj_word.name
            self.output_content += " "

        # удаляю последний пробел
        self.output_content = self.output_content[:-1] 
