class DataLayer:
    def __init__(self):
        self.data = []

    def save_data(self, item):
        self.data.append(item)

    def get_data(self):
        return self.data