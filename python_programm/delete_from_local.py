import os
import json
import sys

sys.path.append(os.getcwd())
from util.functions import print_to_xdot_local

del_word = sys.argv[1]

with open(os.getcwd() + "/graphs/local_graph.json") as local_graph_file:
    local_pairs = json.load(local_graph_file)
    local_graph_file.close()


with open(os.getcwd() + "/graphs/local_graph.json", "w") as local_graph_file:
    copy_pairs = local_pairs.copy()
    for pair in local_pairs:
        if del_word in pair:
            copy_pairs.remove(pair)

    json.dump(copy_pairs, local_graph_file, ensure_ascii=False)
    local_graph_file.close()


try:
    path_del_file = os.getcwd() + "/json/local/" + del_word + ".json"
    os.remove(path_del_file)
except FileNotFoundError:
    pass

# перерисовка
print_to_xdot_local()
