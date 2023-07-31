class Inventory:
    def __init__(self):
        self.items = {}

    def serialize(self):
        return {"items": self.items}

    def deserialize(self, data):
        self.items = data["items"]

    def get_item(self, item_name):
        return self.items.get(item_name)

    def add_item(self, item_name, item_location):
        self.items[item_name] = item_location
        
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            return True
        return False

    def view_inventory(self):
        return self.items
