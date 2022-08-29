import sys
import re
import json

# input_l = ["разница", "1658921963", "1658921962"]

output = {}

count_parameters = 1
for i in sys.argv[1:]:
    match_operator = re.match(r'\D*', i)
    match_parametr = re.match(r'\d*', i)
    if match_operator.group():
        output["оператор"] = i
    if match_parametr.group():
        output["параметр_" + str(count_parameters)] = i
        count_parameters += 1

with open("output.json", 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)


# print(output)

    