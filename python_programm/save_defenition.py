import sys
import json
import os

sys.path.append(os.getcwd())
from util.functions import write_to_local_graph_json, print_to_xdot_local


defenition = {}
defenition['name'] = sys.argv[1]
defenition['definitions'] = sys.argv[2:]

# создание связей слова которое определяется с каждым словом входящим в его состав
for node in defenition['definitions']:
    write_to_local_graph_json([defenition['name'], node])


path_to_file = "json/local/" + str(defenition['name']) + ".json"
if os.path.exists(path_to_file):
    file = open(os.getcwd() + "/" + path_to_file)
    json_file = json.load(file)
    file.close()

    if "definitions" in json_file:
        json_file["definitions"].append(defenition['definitions'])

    with open(path_to_file, 'w') as outfile:
        json.dump(json_file, outfile, ensure_ascii=False)

else:
    with open("json/local/" + str(defenition['name']) + ".json", 'w') as outfile:
        json.dump(defenition, outfile, ensure_ascii=False)

output = {}

output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)

print_to_xdot_local()