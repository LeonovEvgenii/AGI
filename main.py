from class_node import Node

# import re

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

                # print(node.links)

                for link in node.links:
                    f.write("  " + node.name + " -> " + link.name + ";\n")

        
#         for _link in links:
#             f.write("  "+_link[0]+" -> "+_link[1]+";\n")
#         for e in uniq_elements:
#             f.write("  "+e+"\n")
        f.write("}\n")

if __name__ == "__main__":

    # связать с первым
    # отобразить в графе

    stol = Node("стол")
    print(stol.name)
    stul = Node("стул")

    # stol.create_link(stul)
    stol.create_link(stul)

    # stol.links = [stul]

    print(stol.links)
    # print(stul.links)

    draw_graph([stol, stul])

    # print(stol.name)



