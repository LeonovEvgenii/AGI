class _Class():
    def __init__(self, word):
        self.name = word

        # создание файла класса в локальном графе (в любом случае)

        # при смене БД, записи изменяются здесь

        self.list_objects = []

    def __str__(self):
        return self.name
    
    # метод перевода из локального в глобальный, со всеми проверками