import os
import json
import sys

sys.path.append(os.getcwd())
from util.functions import print_to_xdot_global

del_word = sys.argv[1]

with open(os.getcwd() + "/graphs/global_graph.json") as global_graph_file:
    global_pairs = json.load(global_graph_file)
    global_graph_file.close()


with open(os.getcwd() + "/graphs/global_graph.json", "w") as global_graph_file:
    copy_pairs = global_pairs.copy()
    for pair in global_pairs:
        if del_word in pair:
            copy_pairs.remove(pair)

    json.dump(copy_pairs, global_graph_file, ensure_ascii=False)
    global_graph_file.close()


try:
    path_del_file = os.getcwd() + "/json/global/" + del_word + ".json"
    os.remove(path_del_file)
except FileNotFoundError:
    pass

# перерисовка
print_to_xdot_global()

output = {}
output["файл_удален"] = True
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)