"""."""

import json
import os

path_json_local = os.getcwd() + '/json/local/'


def write_to_local_graph_json(input_list_words):
    """."""
    # сейчас образуются пары слов
    # альтернатива сделать связи все со всеми

    # формирование списка пар из входных слов
    input_pairs = []
    for index, word in enumerate(input_list_words):
        input_pair = []
        input_pair.append(word)
        try:
            input_pair.append(input_list_words[index + 1])
            input_pairs.append(input_pair)
        except IndexError:
            if len(input_list_words) == 1:
                input_pairs.append(input_pair)
            break

    # добавить сортировку input_pairs # зачем?
    # зачем я в файле графа в json в ключе links пишу ноды, у которых нет
    # связей?

    # добавление новых пар в список уже существующих
    if os.stat('graphs/local_graph.json').st_size != 0:
        out_json = None
        with open('graphs/local_graph.json') as json_file:
            out_json = json.load(json_file)

            # добавление названий узлов, удаление копий
            out_json['nodes'] = list(
                set((out_json['nodes'] + input_list_words)))

            # добавление связей
            for input_pair in input_pairs:
                if len(input_pair) == 2:
                    if (input_pair in out_json['links']
                            or [
                                input_pair[1],
                                input_pair[0]] in out_json['links']):
                        continue
                    else:
                        out_json['links'].append(input_pair)
                else:
                    if input_pair in out_json['links']:
                        continue
                    else:
                        out_json['links'].append(input_pair)

        with open('graphs/local_graph.json', 'w') as outfile:
            json.dump(out_json, outfile, ensure_ascii=False)

    else:
        # использую список списков т к множества json не поддерживает

        out_json = {}
        out_json['nodes'] = input_list_words
        out_json['links'] = input_pairs

        with open('graphs/local_graph.json', 'w') as outfile:
            json.dump(out_json, outfile, ensure_ascii=False)


def print_to_xdot_global():
    """."""
    input_json = None
    with open('graphs/global_graph.json') as json_file:
        input_json = json.load(json_file)

    file_name = 'graphs/global_graph.dot'
    with open(file_name, 'w') as f:
        f.write('strict graph G {\n')

        for node in input_json['nodes']:
            f.write('"' + node + '"\n')

        for save_pair in input_json['links']:
            f.write('"' + save_pair[0] + '" -- "' + save_pair[1] + '"\n')

        f.write('}\n')


def save_new_nodes(input_list_words):
    """."""
    files = os.listdir(path_json_local)
    for word in input_list_words:
        word_class = word[:word.rfind('$')]

        word_instance = word[word.rfind('$'):]

        path_file_class = 'json/local/' + word_class + '.json'

        if not word_class + '.json' in files:
            definition = {}
            definition['name'] = word_class
            definition['instances'] = []
            definition['instances'].append(word_instance)
            with open(path_file_class, 'w') as outfile:
                json.dump(definition, outfile, ensure_ascii=False)
            outfile.close()
        else:

            definition = None
            with open(path_file_class) as json_file:
                definition = json.load(json_file)

            definition['instances'].append(word_instance)

            file_name = path_file_class
            with open(file_name, 'w') as json_file:
                json.dump(definition, json_file, ensure_ascii=False)
