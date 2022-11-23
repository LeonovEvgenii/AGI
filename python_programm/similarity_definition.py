import json
import os
import sys

search_words = sys.argv[1:]

with open(os.getcwd() + "/graphs/global_graph.json") as json_file:
    save_pairs = json.load(json_file)

    sets = []

    # сужаем поиск
    for word in search_words:
        words_in_pair = set()
        for pair in save_pairs:
            if word in pair:
                pair.remove(word)
                if pair:
                    words_in_pair.add(pair[0])
        sets.append(words_in_pair)

    # пересечение
    rez_set = sets[0]
    for _set in sets:
        try:
            rez_set = rez_set.intersection(_set)
        except IndexError:
            pass

    # так выводится множество
    out_list = list(rez_set)
    print(" ".join(out_list))

output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)