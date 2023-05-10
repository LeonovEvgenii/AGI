class Knowledge_base():
    def __init__(self):
        
        # дискуссионный вопрос о том, какой тип стурктуры должен быть.
        # точно не словарь, т к дубли по названию не допустимы
        # операции над множествами не планируются
        # поэтому остается список

        self.local_nodes = []
        self.local_links = []


    # бесполезный метод на тот случай, если локальный граф хранится  в json файлах
    # может быть переписан, чтобы очищать локальную память без перезагрузки
    def clear_local_graph():

        print("\nочищаю локальный граф\n")

        # f = open('knowledge_base/graphs_links/local_graph.json', 'w') # вынести в класс !!!!!

        with open('knowledge_base/graphs_links/local_graph.dot', 'w') as f:
            f.write("strict graph G {\n")
            f.write("}\n")
        f.close()

        f = open('output.json', 'w')
        f.close()

        try:
            local_files = os.listdir(path_json_local)
        except FileNotFoundError:
            return

        if local_files:
            os.system("rm " + path_json_local + "*")

    