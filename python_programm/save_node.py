import sys
import json

for word in sys.argv[1:]:
    defenition = {}
    defenition['name'] = word
    # defenition['file'] = 

    with open("json/local/" + word + ".json", 'w') as outfile:
        json.dump(defenition, outfile, ensure_ascii=False)

