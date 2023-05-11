from scripts.classes.Knowledge_base import Knowledge_base
from scripts.classes._Class import _Class
from scripts.classes._Object import _Object

class Core():
    def __init__(self):
        self.kb = Knowledge_base()

    
    def proseccing_input_words(self, input_str):
        input_str = input_str.lower()

        punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
        for p in punctuation:
            if p in input_str:
                input_str = input_str.replace(p, '')

        input_list_words = input_str.split(" ")
        
        input_list_words = [ i for i in input_list_words if i ]

        return input_list_words

    def get_input_objects_and_classes(self, local_list_objects, local_list_classes):

        while 1:
            input_str = input("Ввод: ")
            if input_str == "":
                print("Введена пустая строка")
                continue

            input_list_words = self.proseccing_input_words(input_str)

            input_list_objects = []
            input_list_classes = []

            if input_list_words:

                for i, word in enumerate(input_list_words):
                    
                    class_in_list = False

                    for _class in local_list_classes:
                        if _class.name == word:
                            new_object = _Object(_class, i + 1)
                            input_list_objects.append(_Object(_class, i + 1))
                            local_list_objects.append(_Object(_class, i + 1))

                            _class.list_objects.append(new_object)
                            class_in_list = True
                        
                    # Проверки на уже существование класса осуществляются только для локального графа.
                    # Во время выполненения нод может быть косяк, когда сначала поиск идет по локальному графу
                    # потом по глобальному. В слове из локального графа может не оказаться определения.
                    # Но логично, что сначала смотрим на локальный граф, т к это последний контекст.
                    # Сейчас переход в глобальный осуществляется только по команде в ручном режиме.

                    if not class_in_list:
                        new_class = _Class(word)
                        input_list_classes.append(new_class)
                        local_list_classes.append(new_class)

                        new_object = _Object(new_class, i + 1)
                        input_list_objects.append(new_object)
                        local_list_objects.append(new_object)

                        new_class.list_objects.append(new_object)

                return input_list_objects, input_list_classes
            else:
                print("Строка не содержит ни одного ключевого слова")