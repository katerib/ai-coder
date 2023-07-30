from game.inventory import Inventory


class Player:
    def __init__(self, name, starting_room, game_map, objects):
        self.name = name
        self.current_room = starting_room
        self.map = game_map
        self.objects = objects
        self.inventory = Inventory()  # Initialize an empty inventory for the player

    def serialize(self):
        return {
            "name": self.name,
            "current_room": self.current_room["name"],
            "inventory": self.inventory.serialize(),
            "map": self.map.serialize(),
        }
    
    @classmethod
    def deserialize(cls, data, map_obj, objects_obj):
        player = cls(data["name"], None, map_obj, objects_obj)
        player.current_room = map_obj.get_room_by_name(data["current_room"])
        player.inventory.deserialize(data["inventory"])
        return player

    def get_name(self):
        return self.name

    def move(self, destination):
        # Check if the player has all the items
        if len(self.current_room["interactive_items"]) >= 1:
            print("You need to find more items")
            return

        # Get the next room to compare with the destination
        next_room = self.map.get_next_room()

        # Checks for last condition to prevent moving at the last room
        if next_room:
            # Check if command is just room name
            if destination.lower() == next_room["name"].lower():
                self.current_room = next_room
                self.map.set_current_room(self.current_room)
                self.map.increment_room_count()
                print(f"You move to {self.current_room['name']}.")
                return
            # Check if command is a direction
            elif self.map.is_move_valid(destination.lower()):
                # Checks for last condition to prevent moving at the last room
                self.current_room = next_room
                self.map.set_current_room(self.current_room)
                self.map.increment_room_count()
                print(f"You move to {self.current_room['name']}")
                return
            else:
                print("You can't go that way. Try another way: north, south, east, or west.")

        return
    
    def get_interactive_items_descriptions(self):
        descriptions = []
        for item_name in self.current_room["interactive_items"]:
            description = self.objects.get_description(item_name)
            descriptions.append(description)
        return descriptions


    def take_item_from_room(self, item):
        item = item.lower()
        # looks for item and removes it from player room instance

        for room_item in self.current_room["interactive_items"]:
            if item == room_item.lower():
                self.current_room["interactive_items"].remove(room_item)
                self.current_room["isPresent"] = False
                return room_item
        return None
    
    
    def add_item_to_room(self, item):
        self.current_room["interactive_items"].append(item)
        self.objects.set_object_presence(item, True)
        print(f"You've added the {item} to the room.")


    def drop_item(self, item):
        item_data = self.objects.get_object(item)

        inventory_item = self.inventory.get_item(item)
        if inventory_item:
            self.add_item_to_room(item)
            self.inventory.remove_item(item)
            print(f"You dropped the {item}.")
        else:
            print("You don't have that item in your inventory.")
