import json
import os
import sys

def search(input_json, search_words):
    sets = []

    # сужаем поиск
    for word in search_words:
        words_in_pair = set()
        for pair in input_json['links']:
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
    out_str = " ".join(out_list)
    return out_str


search_words = sys.argv[1:]

local_file =  open(os.getcwd() + "/graphs/local_graph.json")
local_json = json.load(local_file)
local_file.close()

str_print = search(local_json, search_words)

if str_print == "":
    global_file =  open(os.getcwd() + "/graphs/global_graph.json")
    global_json = json.load(global_file)
    global_file.close()

    str_print = search(global_json, search_words)

print(str_print)

output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)