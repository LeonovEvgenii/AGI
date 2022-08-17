import sys
import json
import os

# path = os.getcwd() + "/json/local/"
# files = os.listdir(path)


# внешний цикл идет по сущестующим джесонам 
# внутри него то что не закоменчено
# как только есть совпадение, ...придумать
# оновная проблема - не перезаписыать файл, а только ссылки дописать
# возможно придется маленькими 3 функциями, т к брейк через один цил не работатет
# первый цикл должен быть все таки по входным парамтрам, а дальше как хочешь, скорей всего функции

for word in sys.argv[1:]:


    # for file in files:
    #     if file[:-5] == word:
    #         with open(path + file) as json_file:
    #             data = json.load(json_file)
    #             data['link'] = ["сохрани_узлы"] + sys.argv[1:]
    #             json.dump(data, outfile, ensure_ascii=False)
    #         break

    defenition = {}
    defenition['name'] = word
    defenition['link'] = ["сохрани_узлы"] + sys.argv[1:]
    # defenition['file'] = 

    with open("json/local/" + word + ".json", 'w') as outfile:
        json.dump(defenition, outfile, ensure_ascii=False)

# есть косяк, если добавить больше двух нод, то образуются местами связи все 
# со всеми
# но, чтоб нормально рисовалось, ограничения заданы в отрисовке (строгий граф 
# (не более одного ребра) и неориентированный)

