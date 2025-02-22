from scripts.classes.Graph import Graph


# я хотел сделать этот класс абстрактным,
# но тогда в нем ничего нельзя будет реализовывать.
# И нативно в питоне нельзя создавать абстрактные классы,
# а только с библиотекой abc.
# Хочу писать реализацию и не подключать библиотеку,
# поэтому оставлю так.
class Converter():

    # Сначала хотел создать два касса конверторов:
    # один для преобразования контента в граф,
    # другой, наоборот, из графа в контент.
    # Но, т к они могут работать с общими библиотеками, решил оставить в одном классе.
    output_content = None
    input_content = None

    output_graphs = None  # используется для преобразования контента в граф
    input_graphs = None  # используется для преобразования графа в контент

    # input_content -> output_graphs
    # input_graphs -> output_content

    def __init__(self):
        pass

    # решить где и зачем могут использоваться гетеры и сетеры
    # сейчас в них одна строчка и их хочется убрать
    def get_output_graphs(self):
        return self.output_graphs

    def get_input_graphs(self):
        return self.input_graphs

    def get_output_content(self):
        return self.output_content

    def content_to_graphs(self):
        pass

    def graphs_to_content(self):
        pass

    def filter(self):
        pass
