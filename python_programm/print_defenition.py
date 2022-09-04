import json
import sys
import os

with open(os.getcwd() + "/output.json") as json_file:
    data = json.load(json_file)

#### дйсон ouput пустой обработать исключение

    if "необходимость_дальнейшего_выполнения" in data:
        if data["необходимость_дальнейшего_выполнения"] == False:
            exit(0)

path_json = os.getcwd() + "/json/local/"
# path_json = "/home/evgeniy/git/AGI/json/local/"


json_files = os.listdir(path_json)

for file in json_files:
    if sys.argv[1] == file[:-5]:
        with open(path_json + file) as json_file:
            data = json.load(json_file)

            link_without_meta = data['link'].copy()
            link_without_meta.remove("сохрани_определение")

            output_str = " ".join(link_without_meta)
            break


output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)
            
print(output_str)