from scripts.classes.Graph import Graph

class Converter():

    def __init__(self):
        self.input_data = ""
        self.output_graph = Graph("входной_граф")

    def get_graph(self):
        return self.output_graph