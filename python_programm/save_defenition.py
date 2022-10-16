import sys
import json
import os

sys.path.append(os.getcwd())
from utils.functions import write_to_local_graph_json, print_to_xdot


defenition = {}
defenition['name'] = sys.argv[1]
defenition['definition'] = sys.argv[2:]

for node in defenition['definition']:
    write_to_local_graph_json([defenition['name'], node])

with open("json/local/" + str(defenition['name']) + ".json", 'w') as outfile:
    json.dump(defenition, outfile, ensure_ascii=False)

output = {}

output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)

print_to_xdot()