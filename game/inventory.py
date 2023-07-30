class Inventory:
    def __init__(self):
        self.items = {}

    def serialize(self):
        return {"items": self.items}

    def deserialize(self, data):
        self.items = data["items"]

    def get_item(self, item_name):
        return self.items.get(item_name)

    def add_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
                return True
        return False

    def view_inventory(self):
        return self.items
