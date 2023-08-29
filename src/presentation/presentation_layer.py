from business_logic.business_layer import Book,Movie,Password
from data_pesistence.data_layer import DataLayer

class PresentationLayer:
    def __init__(self):
        self.data_layer = DataLayer()
    
    def add_item(self):
        
        item_type = input("Enter the item type (book/movie/password): ")

        if item_type.lower() == "book":
            name = input("Enter the name of the item: ")
            author = input("Enter the author's name: ")
            item = Book(name, author)
        elif item_type.lower() == "movie":
            name = input("Enter the name of the item: ")
            director = input("Enter the movie's director's name: ")
            item = Movie(name, director)
        elif item_type.lower() == "password":
            print("The password must be at least 8 characters long, including at least one uppercase and one lowercase letter, one number and one special character.")
            password = input("Enter a password: ")
            strength = "strong" if Password(password, "").is_secure() else "weak"
            print(f"Password saved (Strength: {strength})")
            item = Password(password, strength)
        else:
            print("Invalid Item Type!")
            return
        
        self.data_layer.save_data(item)

    def display_items(self):
        items = self.data_layer.get_data()
        for item in items:
            print(item.display_info())