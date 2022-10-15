import json
import os
import sys

search_words = sys.argv[1:]

with open(os.getcwd() + "/graphs/local_graph.json") as json_file:
    save_pairs = json.load(json_file)

    
    # после того как связи прокинешь в определении

    # здесь
    # содаешь множество по принципу
    # в паре должен быть один search_words хотя бы
    # количество множеств равно количеству слов в определении

    # потом пересечение множеств
    # в нем должна остаться секунда

    ####

    # for pair in save_pairs:

    #     flag_delete_pair = True

    #     for word in search_words:
    #         if word in pair:
    #             flag_delete_pair = False
    #             break

    #     if flag_delete_pair:
    #         save_pairs.remove(pair)



    # print(save_pairs[0][0])

output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)