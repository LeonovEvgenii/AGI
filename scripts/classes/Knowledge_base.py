import os # !!! починить, убрать, проверить использование

class Knowledge_base():
    def __init__(self):
        
        # дискуссионный вопрос о том, какой тип стурктуры должен быть.
        # точно не словарь, т к дубли по названию не допустимы
        # операции над множествами не планируются
        # поэтому остается список

        # в принятые решения
        # удобно иметь как резделение на классы и объекты
        # так же удобно иметь весь список нод
        # пока оставлю оба варианта, надеюсь багов при переключении все отловлю
        self.local_nodes = []
        self.local_objects = [] 
        self.local_classes = []

        self.local_links = []

        self.path_json_local = os.getcwd() + "/knowledge_base/json_description_words/local/"
        self.path_json_global = os.getcwd() + "/knowledge_base/json_description_words/global/"
        self.path_python_programm = os.getcwd() + "/knowledge_base/python_programm/"


    def create_local_link(self, obj_1, obj_2):

        pair = [obj_1, obj_2]

        # возможная проверка на недопущение дублей пар
        # есть пробелема, но это не точно что set setов делать нелзя
        # по хорошему, local_links сделать множеством, т к оно больше,
        # а перед добалением искать возможную дублирующую пару (для (a, b) искать (b, a) и не добалять вторую)
        self.local_links.append(pair)

        # проверка на существование элемнта не нужна
        # т к из за разного времени ввода экземпляры класса объект всегда будут разные
        # даже если делать проверку, то через оператор in, а не через set в общем списке связей

    def create_node(self, node):
        pass

    def update_node(self, node):
        pass



    # бесполезный метод на тот случай, если локальный граф хранится  в json файлах
    # может быть переписан, чтобы очищать локальную память без перезагрузки
    def clear_local_graph(self):

        print("\nочищаю локальный граф\n")

        # f = open('knowledge_base/graphs_links/local_graph.json', 'w') # вынести в класс !!!!!

        with open('knowledge_base/graphs_links/local_graph.dot', 'w') as f:
            f.write("strict graph G {\n")
            f.write("}\n")
        f.close()

        f = open('output.json', 'w')
        f.close()

        try:
            local_files = os.listdir(self.path_json_local)
        except FileNotFoundError:
            return

        if local_files:
            os.system("rm " + self.path_json_local + "*")

    