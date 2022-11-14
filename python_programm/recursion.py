import sys
import json
import os

goal_word = sys.argv[1]
depth = int(sys.argv[2])

def recursion(goal_word, depth, exception_list):

    if depth < 1:
        return []
    else:
        depth -= 1

    neighbors_list = []

    with open("graphs/local_graph.json") as file_graph:
        data = json.load(file_graph)

        for pair in data:

            if goal_word in pair and pair[0] not in exception_list and pair[1] not in exception_list:
                pair.remove(goal_word)
                neighbors_list.append(pair[0])

    exception_list.append(goal_word)

    all_neighbors = []

    for word in neighbors_list:
        all_neighbors += recursion(word, depth, exception_list)

    if all_neighbors:
        return list(set(all_neighbors))
    else:
        return list(set(neighbors_list))



all_neighbors = recursion(goal_word, depth, [])

print(" ".join(all_neighbors))

output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)