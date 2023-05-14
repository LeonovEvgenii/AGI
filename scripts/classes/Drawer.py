class Drawer():
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.path_local_xdot = "knowledge_base/graphs_links/local_graph.dot"


    def print_to_xdot_local(self):

        # сначала нужно старый файл очистить

        # Источником связей могут служить список или файл json
        # Приоритетный источник список

        with open(self.path_local_xdot, 'w') as f:
            f.write("strict graph G {\n")

            # for _class in self.kb.local_classes:
            #     for i, obj in enumerate(_class.list_objects):
            #         f.write('"' + obj.name + '\n' + str(i + 1) + '"\n')

            for link in self.kb.local_links:
                flag_two = False
                for node in link: # нельзя вязть и просто перебрать элементы т к в множестве так нельзя)
                    if node.__class__.__name__ == "_Object":

                        # print(node)
                        # print(node.link_class.list_objects)
                        number = node.link_class.list_objects.index(node) # оригинальный извращенец

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



        # Старый код чтения из json

        # input_json = None
        # with open("graphs/local_graph.json") as json_file:
        # 	input_json = json.load(json_file)

        # file_name = "graphs/local_graph.dot"
        # with open(file_name, 'w') as f:
        # 	f.write("strict graph G {\n")

        # 	for node in input_json['nodes']:
        # 		f.write('"' + node + '"\n')

        # 	for save_pair in input_json['links']:
        # 		if len(save_pair) == 2: 
        # 			f.write('"' + save_pair[0] + '" -- "' + save_pair[1] + '"\n')
        # 		else:
        # 			f.write('"' + save_pair[0] + '"\n')

        # 	f.write("}\n")

        # здесь так же может быть код открытия в визуализаторе