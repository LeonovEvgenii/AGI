import os
import json
import shutil

from functions_temp import print_to_xdot_global

path_to_local = os.getcwd() + "/json/local/"
path_to_global = os.getcwd() + "/json/global/"

files_local = os.listdir(path_to_local)
files_global = os.listdir(path_to_global)

# for file in files_local:
#     if file not in files_global:
#         shutil.copyfile(path_to_local + file, path_to_global + file)
#     else:
#         pass
#         # добавить пометку о противоречии определений

local_pairs = None
with open(os.getcwd() + "/graphs/local_graph.json") as local_graph_file:
    local_pairs = json.load(local_graph_file)
    local_graph_file.close()


with open(os.getcwd() + "/graphs/global_graph.json", 'w') as global_graph_file:

    meta_words = ["выведи_определение", "выполни_с_параметрами", "на_что_похоже", "привяжи_к _питону", "рекурсия", "сохрани_в_глобальный", "сохрани_определение", "сохрани_узлы"]

    global_pairs = []
    for pair in local_pairs:
        if pair[0] in meta_words or pair[1] in meta_words:
            continue
        else:
            global_pairs.append(pair)

    json.dump(global_pairs, global_graph_file, ensure_ascii=False)
    global_graph_file.close()

print_to_xdot_global()

# local_graph.json скопировать в global_graph.json

# проверять если слова нет, то добавлять
# если слово есть, то доплнить поля (сделаю но не сразу, а когда будет уточнение определений)

# если есть связь со служебным словом, то не добавлять ее
# xdot глобальный перересовать



