import sys
import json
import os

with open(os.getcwd() + "/output.json") as json_file:
    data = json.load(json_file)

    if "необходимость_дальнейшего_выполнения" in data:
        if data["необходимость_дальнейшего_выполнения"] == False:
            exit(0)

path = os.getcwd() + "/json/local/" # !!!!!
# path = "/home/evgeniy/git/AGI/json/local"


output = {}

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
        # пока не потребовалась обработка, если слово есть

        pass

        # with open(path + word + ".json", 'r+') as json_file:
        #     data = json.load(json_file)

        #     if "link" in data:
        #         if not("сохрани_узлы" in data["link"]):
        #             data["link"].append("сохрани_узлы")
        #     else:
        #         data["link"] = []
        #         data["link"].append("сохрани_узлы")

        #     if data['file'] == sys.argv[-1]:
        #         json.dump(defenition, outfile, ensure_ascii=False)
        #         continue
            
    else:

        if word[-3:] == ".py":
            continue

        defenition = {}
        defenition['name'] = word

        if ".py" in sys.argv[-1]:
            defenition['file'] = sys.argv[-1]
            defenition['link'] = ["сохрани_узлы"] + sys.argv[1:-1]
            with open("json/local/" + word + ".json", 'w') as outfile: # !!!!!
            # with open("/home/evgeniy/git/AGI/json/local/" + word + ".json", 'w') as outfile:
                json.dump(defenition, outfile, ensure_ascii=False)
            break

        defenition['link'] = ["сохрани_узлы"] + sys.argv[1:]
        with open("json/local/" + word + ".json", 'w') as outfile: # !!!!!
        # with open("/home/evgeniy/git/AGI/json/local/" + word + ".json", 'w') as outfile:
            json.dump(defenition, outfile, ensure_ascii=False)

# print("сохрани_узлы_выполнилось")

output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)

# есть косяк, если добавить больше двух нод, то образуются местами связи все 
# со всеми
# но, чтоб нормально рисовалось, ограничения заданы в отрисовке (строгий граф 
# (не более одного ребра) и неориентированный)

