from game.inventory import Inventory


class Player:
    def __init__(self, name, starting_room, game_map, objects):
        self.name = name
        self.current_room = starting_room
        self.map = game_map
        self.objects = objects
        self.inventory = Inventory()  # Initialize an empty inventory for the player

    def move(self, direction):
        if direction in self.current_room["valid_moves"].keys() and self.map.is_move_valid(direction):
            if len(self.current_room["interactive_items"]) >= 1:
                print("You need to find more items")
                return
            print(self.current_room["interactive_items"])
            next_room_name = self.map.get_next_room()
            self.current_room = next_room_name
            # self.current_room = self.map.get_room(next_room_name)
            print(f"You move to {self.current_room['name']}")
        else:
            print("You can't go that way.")
        return

    def take_item_from_room(self, item):
        item = item.lower()
        # looks for item and removes it from player room instance

        for room_item in self.current_room["interactive_items"]:
            # if item == room_item.lower():
            if item in self.current_room["interactive_items"]:
                self.current_room["interactive_items"].remove(room_item)
                return room_item
        return None
