import sys
import json
import os


path = os.getcwd() + "/json/local/"

def check_file(word):
    files = os.listdir(path)
    for file in files:
        if file[:-5] == word:
            # print(word, " уже существует")
            return True

    # print(word, " еще не существует")
    return False


for word in sys.argv[1:]:
    if check_file(word):
        pass
        # ???
        # пока работает и ладно
        # вообще, должно добавлять только ссылки в существующий файл
        # with open(path + word + ".json") as json_file:
        #     data = json.load(json_file)
        #     data['link'] = ["сохрани_узлы"] + sys.argv[1:]
            # json.dump(data, outfile, ensure_ascii=False)
    else:
        defenition = {}
        defenition['name'] = word

        if ".py" in sys.argv[-1]:
            defenition['file'] = sys.argv[-1]
            with open("json/local/" + word + ".json", 'w') as outfile:
                json.dump(defenition, outfile, ensure_ascii=False)
            break

        defenition['link'] = ["сохрани_узлы"] + sys.argv[1:]
        with open("json/local/" + word + ".json", 'w') as outfile:
            json.dump(defenition, outfile, ensure_ascii=False)


print("ok")



# есть косяк, если добавить больше двух нод, то образуются местами связи все 
# со всеми
# но, чтоб нормально рисовалось, ограничения заданы в отрисовке (строгий граф 
# (не более одного ребра) и неориентированный)

