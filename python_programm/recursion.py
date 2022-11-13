import sys
import json
import os

goal_word = sys.argv[1]
depth = int(sys.argv[2])

def recursion(goal_word, depth):

    if depth < 1:
        return []
    else:
        depth -= 1

    neighbors_list = []

    with open("graphs/local_graph.json") as file_graph:
        data = json.load(file_graph)

        for pair in data:

            # проблема
            # не использовать в списке кандидатов на продолжние
            # рекурсии те слова от которых мы пришли.
            # методика исключения слова мне нравится
            # но не понятно как начать, т к на превом шаге 
            # не проходим сквозь нижнее условие исключения

                if goal_word in pair:
                    pair.remove(goal_word)
                    neighbors_list.append(pair[0])

    all_neighbors = []

    for word in neighbors_list:
        all_neighbors += recursion(word, depth)

    # вариант вывода с элементами находящимися длаеко (на том уровне
    #  рекурсии который указан в параметре)
    # работает с багом на 2 уровне (выводит элементы, от которых пришел)
    # есть косяк, если дошел до самой глубокой токи в графе
    # в зависимости от четности глубины рекурсии может то возваращаться на
    #  1 элемент назад, то нормально работать
    if all_neighbors:
        all_items = set(all_neighbors) - set(neighbors_list)
        all_items = list(all_items)
        return all_items
    else:
        return neighbors_list



all_neighbors = recursion(goal_word, depth)

print(" ".join(all_neighbors))

output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)