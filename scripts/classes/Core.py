from scripts.classes.Knowledge_base import Knowledge_base
from scripts.classes._Class import _Class
from scripts.classes._Object import _Object
from scripts.classes.Drawer import Drawer

class Core():
    def __init__(self):
        self.kb = Knowledge_base()
        self.drawer = Drawer(self.kb)

    
    def formatting(self, input_str):
        input_str = input_str.lower()

        punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
        for p in punctuation:
            if p in input_str:
                input_str = input_str.replace(p, '')

        input_list_words = input_str.split(" ")
        
        input_list_words = [ i for i in input_list_words if i ]

        return input_list_words


    def input_words(self):

        while 1:
            input_str = input("Ввод: ")
            if input_str == "":
                print("Введена пустая строка")
                continue

            input_list_words = self.formatting(input_str)

            input_objects = []
            input_classes = []

            if input_list_words:

                for i, word in enumerate(input_list_words):
                    
                    class_in_list = False

                    for _class in self.kb.local_classes:
                        if _class.name == word:
                            new_object = _Object(_class, i + 1)
                            input_objects.append(new_object)
                            self.kb.local_objects.append(new_object)

                            _class.list_objects.append(new_object)
                            class_in_list = True
                        
                    # Проверки на уже существование класса осуществляются только для локального графа.
                    # Во время выполненения нод может быть косяк, когда сначала поиск идет по локальному графу
                    # потом по глобальному. В слове из локального графа может не оказаться определения.
                    # Но логично, что сначала смотрим на локальный граф, т к это последний контекст.
                    # Сейчас переход в глобальный осуществляется только по команде в ручном режиме.

                    if not class_in_list:
                        new_class = _Class(word)
                        input_classes.append(new_class)
                        self.kb.local_classes.append(new_class)

                        new_object = _Object(new_class, i + 1)
                        input_objects.append(new_object)
                        self.kb.local_objects.append(new_object)

                        new_class.list_objects.append(new_object)

                # не забываем, что input_list_classes только новые классы возвращаются
                # если ничего не вернулось, значит они уже есть в local_list_classes
                return input_objects, input_classes
            else:
                print("Строка не содержит ни одного ключевого слова")


    def test_intput_lists(self, input_objects, input_classes):
        print("список входных объектов")
        [ print(i) for i in input_objects ]
        print("список входных классов")
        [ print(i) for i in input_classes ]

        print("\nсписок локальных объектов")
        [ print(i) for i in self.kb.local_objects ]
        print("список локальных классов")
        [ print(i) for i in self.kb.local_classes ]

    
    def write_local_links(self, input_objects, input_classes):
        
        count_obj = len(input_objects)
        for index, obj in enumerate(input_objects):
            
            if index + 1 != count_obj:
                self.kb.create_local_link(obj, input_objects[index + 1])

        for _class in input_classes:
            for obj in _class.list_objects:
                self.kb.create_local_link(_class, obj)


    def test_links(self):

        # отрисовка пар
        for i in self.kb.local_links:
            print("пара")
            for j in i:
                print(j.name, j.__class__.__name__)

