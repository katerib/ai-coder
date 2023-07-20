from game.inventory import Inventory


class Player:
    def __init__(self, name, starting_room, game_map):
        self.name = name
        self.current_room = starting_room
        self.map = game_map  # Store a reference to the game map
        self.inventory = Inventory()  # Initialize an empty inventory for the player

    def move(self, direction):
        if direction in self.current_room["connected_rooms"]:
            next_room_name = self.current_room["connected_rooms"][direction]
            self.current_room = self.map.get_room(next_room_name)
            print(f"You move to {self.current_room['name']}")
        else:
            print("You can't go that way.")

    def take_item(self, item):
        if item in self.current_room["items"]:
            item_data = self.current_room["items"][item]
            self.inventory.add_item(item_data["name"])
            del self.current_room["items"][item]
            print(f"You picked up {item_data['name']}")
        else:
            print("There is no such item in this room.")

    def use_item(self, item):
        item_data = self.inventory.get_item(item)
        if item_data:
            # Implement the logic for using the item
            print(f"You used {item_data['name']}")
        else:
            print("You don't have that item in your inventory.")
