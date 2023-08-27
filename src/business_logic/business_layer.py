class Item:
    def __init__(self, name):
        self.name = name

    def display_info(selft):
        pass  

class Book(Item):
    def __init__(self, name, author):
        super().__init__(name)
        self.author = author

    def display_info(self):
        return f"Book: {self.name} by {self.author}"

class Movie(Item):
    def __init__(self, name, director):
        super().__init__(name)
        self.director = director

    def display_info(self):
        return f"Movie: {self.name} directed by {self.director}"