import sys
import os

sys.path.append(os.getcwd())
from util.functions import write_to_local_graph_json, print_to_xdot_local, save_new_nodes

#unix
import time
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