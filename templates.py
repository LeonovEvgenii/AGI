import random

# in_str = "00010000100000100000100010"
# in_str = "00010000100000100000100010"
in_str = "00011000010000010011000100010"

# for i in range(1000):
#     in_str += str(random.randint(0,1))

# print(in_str)

# for n in range(1,6):
#     template = "1"*n
#     print(template)



# one = "1"
# two = "11"
# tree = "111"

# telpate = tree

# len_templ = len(telpate)
# for i, val in enumerate(in_str):
#     # print(in_str[i:i+len_templ])
#     if telpate in in_str[i:i+len_templ]:
#         print(i)

len_window = 3

templates = []

for i, val in enumerate(in_str):
    current_window = in_str[i:i+len_window]
    
    if len(current_window) < len_window:
        break

    if current_window not in templates:
        templates.append(current_window)


print(templates)