from scripts.classes._Class import _Class

class First_born(_Class):

    def __init__(self, word):
        super().__init__(word)

        self.path_python_file = ""

    def __str__(self) -> str:
        return "первородная: " + self.name