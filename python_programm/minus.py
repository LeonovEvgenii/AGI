import sys
import json
import os



with open(os.getcwd() + "/output.json") as json_file:
    data = json.load(json_file)

    rezult = int(data["параметр_1"]) - int(data["параметр_2"])
    
    output = {}

    output["ответ"] = rezult

with open(os.getcwd() + "/output.json", 'w') as json_file:
    json.dump(output, json_file, ensure_ascii=False)

    print(output)


# if __name__ == "__main__":
#     with open(os.getcwd() + "/output.json") as json_file:
#     data = json.load(json_file)

#     print(type(data))