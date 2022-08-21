import sys
import os
import json
import subprocess

# print(sys.argv)

# ищем дсон с 1 параметром

# и выполняем его уже




path_json = os.getcwd() + "/json/local/"
json_files = os.listdir(path_json)

path_python = os.getcwd() + "/python_programm"

for file in json_files:
    if sys.argv[1] == file[:-5]:
        with open(path_json + file) as json_file:
            data = json.load(json_file)

    #         # !!! если нет питона то не выполняем, а так все слова в предложении выполняются
            if "file" in data: 

                list_without_run_word = sys.argv[2:]

                print(list_without_run_word)

                output = subprocess.check_output(["python3", path_python + "/" + data["file"]] + list_without_run_word, encoding='utf-8')

            # !!! нужно как то вернуть информацию наверх, 
            # что остальные параметры не выполняем

            # print("не выполняем")
    #             # вывод обрантый никак не обрабатываю

                print("ok")
