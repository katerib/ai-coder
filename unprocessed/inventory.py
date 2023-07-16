class Inventory:
    def __init__(self, data):
        self.items = data

    def get_item(self, item_name):
        return self.items[item_name]
