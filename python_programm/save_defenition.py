import sys
import json


defenition = {}
defenition['name'] = sys.argv[1]
defenition['definition'] = sys.argv[2:]

with open("json/local/" + str(defenition['name']) + ".json", 'w') as outfile:
    json.dump(defenition, outfile, ensure_ascii=False)

output = {}

output["необходимость_дальнейшего_выполнения"] = False
with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)

