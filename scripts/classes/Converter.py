from scripts.classes.Graph import Graph

class Converter():

    output_content = None

    def __init__(self):
        self.input_data = ""
        self.output_graph = Graph("входной_граф")

    def get_graph(self):
        return self.output_graph

    def get_content(self):
        return self.output_content # можно даже не использовать в этом методе и выше слово output

    def content_to_graph(self):
        pass

    def graph_to_content(self):
        pass

    def filter(self):
        pass