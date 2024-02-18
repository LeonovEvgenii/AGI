# будут ли бругие типы нод, например датчик?

class Node():
    
    def __init__(self, name):
        self.name = name

    def return_name_for_draw(self):
        pass

    def __str__(self):
        return "нода: " + self.name