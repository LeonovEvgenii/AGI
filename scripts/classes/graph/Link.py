class Link():

    def __init__(self, one_node, two_node):
        self.one_node = one_node
        self.two_node = two_node

    def __str__(self) -> str:
        return "ссылка: " + str(self.one_node) + " -> " + str(self.two_node)
        
