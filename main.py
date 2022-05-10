from class_node import Node
import re

# while 1:
#     # чтение входной строки
#     input_str = str(input("введи предложение: "))

#     # определение вопроса или утвержения
#     if input_str[-1:] == "?":
#         q = True
#         input_str = input_str.replace('?', '')

#     # перевод входной строки в список
#     list_word = input_str.split(" ")

#     # чтение существующего графа
#     with open("graph.dot", 'r') as f:
#         lines = f.readlines()

#     # разделение на элементы и связи
#     elements = set()
#     links = set()
#     elements_link = set()
#     for line in lines[1:-1]:
#         l = re.sub(" |;|\n", "", line)
#         l = l.split("->")
#         if len(l) > 1:
#             links.add((l[0], l[1]))
#             elements_link.add(l[0])
#             elements_link.add(l[1])
#         for _ in l:
#             elements.add(_)

#     if q:
#         if list_word[0] in elements:
#             print("я знаю: "+str(list_word[0]))
#         else:
#             print("я не знаю: "+str(list_word[0])+" запомню его")
        

#     # добавление несуществующих элементов и связей
#     for i, word in enumerate(list_word):
#         if word not in elements:
#             elements.add(word)

#         try:
#             next_word = list_word[i+1]
#             new_link = (word, next_word)
#             if new_link not in links:
#                 links.add(new_link)
#                 elements_link.add(word)
#                 elements_link.add(next_word)
#         except IndexError:
#             break
        
#     # выделение несвязанных элементов
#     uniq_elements = elements.difference(elements_link)

#     # print("все элементы: "+str(elements))
#     # print("элементы в не связях: "+str(uniq_elements))
#     # print("связи: "+str(links))

#     # запись в файл
#     with open("graph.dot", 'w') as f:
#         f.write("digraph G {\n")
#         for _link in links:
#             f.write("  "+_link[0]+" -> "+_link[1]+";\n")
#         for e in uniq_elements:
#             f.write("  "+e+"\n")
#         f.write("}\n")

def draw_graph(list_nodes):
    with open("graph.dot", 'w') as f:
        f.write("digraph G {\n")
        for node in list_nodes:
            f.write("  " + node.name + ";\n")
            if len(node.links) > 0:
                for link in node.links:
                    f.write("  " + node.name + " -> " + link.name + ";\n")
        f.write("}\n")

def get_obj_graph():
    with open("graph.dot", 'r') as f:
        lines = f.readlines()

        elements = set()
        links = set()
        elements_link = set()
        for line in lines[1:-1]:
            l = re.sub(" |;|\n", "", line)
            if l == '':
                continue
            l = l.split("->")
            if len(l) > 1:
                links.add((l[0], l[1]))
                elements_link.add(l[0])
                elements_link.add(l[1])
            
            for _ in l:
                elements.add(_)

    graph_list_nodes = []
    for element in elements:
        graph_list_nodes.append(Node(element))

    # добавляю ссылки в список нод
    for link in links:
        for node in graph_list_nodes:
            if node.name == link[0]:
                for node_2 in graph_list_nodes:
                    if node_2.name == link[1]:
                        node.create_link(node_2)

    return graph_list_nodes

def convert_words_to_nodes(input_list_words):
    input_list_nodes = []

    # if len(input_list_words)  1:

    # for i, word in enumerate(input_list_words):
    #     node = Node(word)
        
    #     try:
    #         node_2 = Node(input_list_words[i+1])
    #         node.create_link(node_2)
    #         input_list_nodes.append(node)
    #     except IndexError:
    #         break
        

    return input_list_nodes


if __name__ == "__main__":


    while 1:
        graph_list_nodes = get_obj_graph()
        input_str = input("Введи факт: ")
        input_list_words = input_str.split(" ")

        input_list_nodes = convert_words_to_nodes(input_list_words)

        # Входные слова преобразовать в формат узлов
        # Если узел не входит в текущий граф, то добавить

        
      
        graph_list_nodes += input_list_nodes

        draw_graph(graph_list_nodes)

        # есть баги
        # повторно записывается уже существующий элемент
        # если граф пустой ничего не записывается или ставится точка с запятой
        # одиночные элементы не добавляются

    # _1 = Node("1")
    # _2 = Node("2")
    # _3 = Node("3")
    # _4 = Node("4")

    # _1.create_link(_2)
    # _1.create_link(_3)
    # _2.create_link(_1)
    # _2.create_link(_4)

    # draw_graph([_1, _2, _3, _4])




