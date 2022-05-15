class MetaEnum(type):
    def __contains__(cls, x):
            print("cont")


class My_list(list):
    def __init__(self):
        super().__init__()


class My_var():
    def __init__(self, var):
        self.name = var

    def __contain__(self, key):
        print("сравниваю ", key)

class My_var_2():
    def __init__(self, var):
        self.name = var

    def __contain__(self, key):
        print("2 сравниваю ", key)


_1 = My_var("1")
_2 = My_var("1")
_3 = My_var("1")

_4 = My_var_2("1")

# print(_1.__contain__("s"))

a = My_list()

# a.append(_1)
# a.append(_2)
# a.append(_3)

# print(_1 in a)

if _1 in a:
    print("входит")
else:
    print("не входит")
