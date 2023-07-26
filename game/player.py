from game.inventory import Inventory


class Player:
    def __init__(self, name, starting_room, game_map, objects):
        self.name = name
        self.current_room = starting_room
        self.map = game_map
        self.objects = objects
        self.inventory = Inventory()  # Initialize an empty inventory for the player

    def get_name(self):
        return self.name

    def move(self, direction):
        if self.map.is_move_valid(direction):
        # if direction in self.current_room["valid_moves"] and self.map.is_move_valid(direction):
            if len(self.current_room["interactive_items"]) >= 1:
                print("You need to find more items")
                return
            # print(self.current_room["interactive_items"])
            next_room_name = self.map.get_next_room()
            self.current_room = next_room_name
            self.map.set_current_room(self.current_room)
            # self.current_room = self.map.get_room(next_room_name)
            print(f"You move to {self.current_room['name']}")
        else:
            print("You can't go that way.")
        return

    def take_item_from_room(self, item):
        item = item.lower()
        # looks for item and removes it from player room instance

        for room_item in self.current_room["interactive_items"]:
            if item == room_item.lower():
                self.current_room["interactive_items"].remove(room_item)
                return room_item
        return None
    
 
    def drop_item(self, item):
        item_data = self.objects.get_object(item)
        
        inventory_item = self.inventory.get_item(item)
        if inventory_item:
            if item_data["equipped"]:
                # Mark the item as not equipped if equipped
                self.objects.mark_item_as_not_equipped(item)
            # Add the item to the room and remove from inventory
            self.current_room["interactive_items"].append(item)
            self.inventory.remove_item(item)
            print(f"You dropped the {item}.")
        else:
            print("You don't have that item in your inventory.")

