"""Файл слова 'время'."""

import os
import sys
import time

from scripts.util.functions import (
    print_to_xdot_local,
    save_new_nodes,
    write_to_local_graph_json)


sys.path.append(os.getcwd())

# unix
unix_time = str(round(time.time()))

# человекочитаемый
# from datetime import datetime
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time)

print(unix_time)

input_list_words = sys.argv[1:]
input_list_words.append(unix_time)

write_to_local_graph_json(input_list_words)
print_to_xdot_local()
save_new_nodes(input_list_words)
