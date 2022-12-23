import random

in_str = ""

for i in range(1000):
    in_str += str(random.randint(0,1))

# print(in_str)

for n in range(1,6):
    template = "1"*n
    print(template)



# templates = []

# one = "1"
# two = "11"
# tree = "111"

# telpate = tree

# len_templ = len(telpate)
# for i, val in enumerate(in_str):
#     # print(in_str[i:i+len_templ])
#     if telpate in in_str[i:i+len_templ]:
#         print(i)