import json
import sys
import os

def return_definition(path, name):
    output_str = ""
    
    json_files = os.listdir(path)

    for file in json_files:
        if name == file[:-5]:
            with open(path_json + file) as json_file:
                data = json.load(json_file)

                definition = data['definitions'].copy()

                output_str = " ".join(definition[0])
                break
    
    return output_str

if os.stat(os.getcwd() + "/output.json").st_size != 0:
    # не пустой файл
    with open(os.getcwd() + "/output.json") as json_file:
        # if json_file != None:
        data = json.load(json_file)

    #### дйсон ouput пустой обработать исключение

        if "необходимость_дальнейшего_выполнения" in data:
            if data["необходимость_дальнейшего_выполнения"] == False:
                exit(0)


output_str = ""

path_json = os.getcwd() + "/json/local/"
output_str = return_definition(path_json, sys.argv[1])

if output_str == "":
    path_json = os.getcwd() + "/json/global/"
    output_str = return_definition(path_json, sys.argv[1])


output = {}
output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)
            
print(output_str)