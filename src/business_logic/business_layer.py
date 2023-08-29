import re

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

class Password(Item):
    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength
    
    def display_info(self):
        return f"Password: {self.name} (Strength: {self.strength})"
    
    def is_secure(self):
        # Use a regular expression to check password strength
        # For example, let's say a strong password must have at least 8 characters, 
        # including at least one uppercase letter, one lowercase letter, one digit, and one special character.
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        return re.match(pattern, self.name) 