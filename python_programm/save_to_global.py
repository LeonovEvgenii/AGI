import os
import json
import shutil
import sys

sys.path.append(os.getcwd())
from util.functions import print_to_xdot_global


path_to_local = os.getcwd() + "/json/local/"
path_to_global = os.getcwd() + "/json/global/"

# копирование файлов слов .json
files_local = os.listdir(path_to_local)
files_global = os.listdir(path_to_global)

for file in files_local:
    if file not in files_global:
        shutil.copyfile(path_to_local + file, path_to_global + file)
    else:
        
        # # дополнить поля когда будет уточнение определений

        # local_file = open(path_to_local + file)
        # global_file = open(path_to_global + file)

        # data_local = json.load(local_file)
        # data_global = json.load(global_file)

        # if "file" in data_local:
        #     shutil.copyfile(path_to_local + file, path_to_global + file)
        # else:
        #     print("локальное слово больше глоабального", str(file))
        
        # local_file.close()
        # global_file.close()

        pass


# копирование связей .json
json_local = None
with open(os.getcwd() + "/graphs/local_graph.json") as local_graph_file:
    json_local = json.load(local_graph_file)
    local_graph_file.close()

global_graph_file = open(os.getcwd() + "/graphs/global_graph.json")
json_global = json.load(global_graph_file)
global_graph_file.close()

with open(os.getcwd() + "/graphs/global_graph.json", "w") as global_graph_file:
    meta_words = ["очисти_граф", "очищаю", "локальный", "граф", "выведи_определение", "выполни_с_параметрами", "на_что_похоже", "привяжи_к _питону", "рекурсия", "сохрани_в_глобальный", "сохрани_определение", "сохрани_узлы"]

    json_global['nodes'] = list(set((json_global['nodes'] + json_local['nodes'])))

    for pair in json_local['links']:
        if pair[0] in meta_words or pair[1] in meta_words:
            continue
        else:
            if pair not in json_global['links']:
                json_global['links'].append(pair)

    json.dump(json_global, global_graph_file, ensure_ascii=False)
    global_graph_file.close()

# перерисовка
print_to_xdot_global()



