from business_logic.business_layer import Book,Movie
from data_pesistence.data_layer import DataLayer

class PresentationLayer:
    def __init__(self):
        self.data_layer = DataLayer()
    
    def add_item(self):
        name = input("Enter the name of the item: ")
        item_type = input("Enter the item type (book/movie): ")

        if item_type.lower() == "book":
            author = input("Enter the author's name: ")
            item = Book(name, author)
        elif item_type.lower() == "movie":
            director = input("Enter the movie's director's name: ")
            item = Movie(name, director)
        else:
            print("Invalid Item Type!")
            return
        
        self.data_layer.save_data(item)

    def display_items(self):
        items = self.data_layer.get_data()
        for item in items:
            print(item.display_info())