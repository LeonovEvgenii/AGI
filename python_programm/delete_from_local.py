import os
import json
import shutil
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
    path_del_file = os.listdir(os.getcwd() + "/json/local/" + del_word + ".json")
    print(path_del_file)
    # shutil.rmtree()
    # os.remove(os.listdir(os.getcwd() + "/json/local/" + del_word + ".json"))
except FileNotFoundError:
    pass


# перерисовка
print_to_xdot_local()



# # копирование файлов слов .json
# files_local = os.listdir(path_to_local)
# files_global = os.listdir(path_to_global)

# for file in files_local:
#     if file not in files_global:
#         shutil.copyfile(path_to_local + file, path_to_global + file)
#     else:
        
#         # # дополнить поля когда будет уточнение определений

#         # local_file = open(path_to_local + file)
#         # global_file = open(path_to_global + file)

#         # data_local = json.load(local_file)
#         # data_global = json.load(global_file)

#         # if "file" in data_local:
#         #     shutil.copyfile(path_to_local + file, path_to_global + file)
#         # else:
#         #     print("локальное слово больше глоабального", str(file))
        
#         # local_file.close()
#         # global_file.close()

#         pass


# # копирование связей .json
# local_pairs = None
# with open(os.getcwd() + "/graphs/local_graph.json") as local_graph_file:
#     local_pairs = json.load(local_graph_file)
#     local_graph_file.close()

# global_graph_file = open(os.getcwd() + "/graphs/global_graph.json")
# global_pairs = json.load(global_graph_file)
# global_graph_file.close()

# with open(os.getcwd() + "/graphs/global_graph.json", "w") as global_graph_file:
#     meta_words = ["очисти_граф", "очищаю", "локальный", "граф", "выведи_определение", "выполни_с_параметрами", "на_что_похоже", "привяжи_к _питону", "рекурсия", "сохрани_в_глобальный", "сохрани_определение", "сохрани_узлы"]

#     # global_pairs = []
#     for pair in local_pairs:
#         if pair[0] in meta_words or pair[1] in meta_words:
#             continue
#         else:
#             if pair not in global_pairs:
#                 global_pairs.append(pair)

#     json.dump(global_pairs, global_graph_file, ensure_ascii=False)
#     global_graph_file.close()

# # перерисовка
# print_to_xdot_global()



