from scripts.classes.Converter import Converter


class Console(Converter):

    output_content = ""

    def __init__(self):
        super().__init__()

    def content_to_graph(self, text=None):
        if text:
            self.paste_input_data(text)
        else:
            self.read_input_data()

        return self.get_graph()

    def read_input_data(self):

        while 1:
            input_str = input("Ввод: ")
            if input_str == "":
                print("Введена пустая строка")
                continue
            else:
                break

        self.paste_input_data(input_str)


    def __formatting(self, input_str):
        input_str = input_str.lower()

        punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
        for p in punctuation:
            if p in input_str:
                input_str = input_str.replace(p, '')

        input_list_words = input_str.split(" ")
        
        input_list_words = [ i for i in input_list_words if i ]

        return input_list_words

    def write_output_data(self, output_graph):

        for link in output_graph.links:

            print(link)

            pass

    def paste_input_data(self, input_str):
        input_list_words = self.__formatting(input_str)

        if input_list_words:

            old_node = None
            
            for i, word in enumerate(input_list_words):

                # необходимо просмотреть функцию words_to_lists
                # нужно связи в выходной граф добавлять
                # потренироваться на настощих первородных вершинах
                # определить когда вершина меняется с первородной на второроднуюы
                # вспомнить как работать с новыми вершинами и уже известными для первородных и второродных
                # служебные слова сохранения определений
                # служебные слова записать в инструкцию
                # служебные слова по сути первородные ноды
                # сначало сохранение перворобной ноды без ссылки на питон, только название сохранить
                # получестя, все незнакомые слова становятся первородными, до указангия определения
                # первородные могут исполняться, везде должны быть заглушки от отсутсвия ссылки на скрипт
                

                new_node = self.output_graph.add_node(word, number_in_sentence = i + 1)

                if old_node:
                    self.output_graph.add_link(old_node, new_node)

                old_node = new_node

            # return self.output_graph # !!!!!
            
        else:
            print("Строка не содержит ни одного ключевого слова")

    def graph_to_content(self, output_graph, print=False):
        # return super().graph_to_content() анализировать необходимость
        if print:
            self.write_output_data(output_graph)
            print()
        else:
            self.write_output_data(output_graph)


        return self.get_content()
