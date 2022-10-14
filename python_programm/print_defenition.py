import json
import sys
import os

if os.stat(os.getcwd() + "/output.json").st_size != 0:
    # не пустой файл
    with open(os.getcwd() + "/output.json") as json_file:
        # if json_file != None:
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

            definition = data['definition'].copy()

            output_str = " ".join(definition)
            break


output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)
            
print(output_str)