# файл используется еще из subprocess, а там другой sys.path
# абсолютные импорты для добавления в sys.path использовать не хочется
# sys.path.append("/home/evgeniy/git/AGI/scripts/classes")
try:
    from scripts.classes.graph.node.Node import Node
except ModuleNotFoundError:
    from Node import Node


class _Class(Node):

    def __init__(self, word):

        # думал о создании объекта в конструкторе
        # отказался от это мысли

        super().__init__(word)

        self.dict_objects = {}

        # питоновская программа хранится как имя файла или путь к файлу, т к
        # код в классе не должен меняться. Если делать функциями или импортами,
        # то придется на все определения делать все
        # функции/импорты и они постоянно будут пополняться.
        self.name_python_program = ''
        self.definitions = []
        self.count_obj = 0

    def add_obj(self, new_object):

        self.dict_objects[self.count_obj] = new_object
        new_object.id = self.count_obj
        self.count_obj += 1

    def __str__(self) -> str:
        return 'класс: ' + self.name

    # метод перевода из локального в глобальный, со всеми проверками
    def local_to_global(self):
        pass

    def get_type(self):
        return '_cls'
