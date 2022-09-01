import sys
import json
import os



with open(os.getcwd() + "/output.json") as json_file:
    data = json.load(json_file)

    if "необходимость_дальнейшего_выполнения" in data:
        if data["необходимость_дальнейшего_выполнения"] == False:
            exit(0)

    rezult = int(data["параметр_1"]) - int(data["параметр_2"])
    
    # output = {}

    # output["ответ"] = rezult
    output = rezult

with open(os.getcwd() + "/output.json", 'w') as json_file:
    json.dump(output, json_file, ensure_ascii=False)

    print(output)


# if __name__ == "__main__":
#     with open(os.getcwd() + "/output.json") as json_file:
#     data = json.load(json_file)

#     print(type(data))