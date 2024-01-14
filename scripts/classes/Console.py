from scripts.classes.Converter import Converter
from scripts.classes.First_born import First_born

class Console(Converter):

    def __init__(self):

        super().__init__()

        input_data = ""

    def read_input_data(self):

        while 1:
            input_str = input("Ввод: ")
            self.input_str = input_str
            if input_str == "":
                print("Введена пустая строка")
                continue

            input_list_words = self.formatting(input_str)

            if input_list_words:
                
                for word in input_list_words:

                    # необходимо просмотреть функцию words_to_lists
                    # нужно связи в выходной граф добавлять
                    # потренироваться на настощих вервородных вершинах
                    # определить когда вершина меняется с первородной на второроднуюы
                    # вспомнить как работать с новыми вершинами и уже известными для первородных и второродных
                    # служебные слова сохранения определений
                    # служебные слова записать в инструкцию
                    # служебные слова по сути первородные ноды
                    # сначало сохранение перворобной ноды без ссылки на питон, только название сохранить
                    # получестя, все незнакомые слова становятся первородными, до указангия определения
                    # первородные могут исполняться, везде должны быть заглушки от отсутсвия ссылки на скрипт
                    f1 = First_born(word)
                    self.output_graph.add_node(f1)

                break

                # input_objects, input_classes = self.words_to_lists(input_list_words)
                # return input_objects, input_classes
                
            else:
                print("Строка не содержит ни одного ключевого слова")

    def formatting(self, input_str):
        input_str = input_str.lower()

        punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
        for p in punctuation:
            if p in input_str:
                input_str = input_str.replace(p, '')

        input_list_words = input_str.split(" ")
        
        input_list_words = [ i for i in input_list_words if i ]

        return input_list_words

    def words_to_lists(self, input_list_words):

        input_objects = []
        input_classes = []

        for i, word in enumerate(input_list_words):
                    
            class_in_list = False

            for _class in self.kb.local_classes:
                if _class.name == word:
                    new_object = _Object(_class, i + 1)
                    _class.add_obj(new_object)
                    self.kb.create_object(new_object)

                    input_objects.append(new_object)
                    self.kb.local_objects.append(new_object)


                    class_in_list = True
                
            # Проверки на уже существование класса осуществляются только для локального графа.
            # Во время выполненения нод может быть косяк, когда сначала поиск идет по локальному графу
            # потом по глобальному. В слове из локального графа может не оказаться определения.
            # Но логично, что сначала смотрим на локальный граф, т к это последний контекст.
            # Сейчас переход в глобальный осуществляется только по команде в ручном режиме.

            if not class_in_list:
                new_class = _Class(word)

                # если в классах класс и объект создаются и добаляются отдельно,
                # (где то им все равно приходится по отдельности создаваться)
                # то и в базе знаний сделаю отдельные методы для работы с ними
                # так же в данном методе уже производится проверка о необходимости создания класса
                self.kb.create_class(new_class)

                input_classes.append(new_class)
                self.kb.local_classes.append(new_class)

                new_object = _Object(new_class, i + 1)
                new_class.add_obj(new_object) # можно спрятать внутрь конструктора объекта
                self.kb.create_object(new_object)

                # ответить на вопросы:
                # пареметры в функции kb передаются в виде объетов или в виде строк
                # функции kb помимо всего делаемого, возвращают созданный объект
                # содаваться могут class obj py def link, они все возвращаемыми объектами будут
                # проверить не полностью на диалоге секунда
                # может там и другие ключевые слова чинить придется
                # self.kb.create_def("333", [new_object.name, new_object.name])

                input_objects.append(new_object)
                self.kb.local_objects.append(new_object)


        # не забываем, что input_list_classes только новые классы возвращаются
        # если ничего не вернулось, значит они уже есть в local_list_classes
        return input_objects, input_classes

    def text_to_graph():
        pass

