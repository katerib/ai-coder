from game.inventory import Inventory


class Player:
    def __init__(self, name, starting_room, game_map, objects):
        self.name = name
        self.current_room = starting_room
        self.map = game_map
        self.objects = objects
        self.inventory = Inventory()  # Initialize an empty inventory for the player
        self.room_history = []


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
        self.room_history.append(self.current_room)


        # Checks for last condition to prevent moving at the last room
        if next_room:
            # Check if command is just room name
            if destination.lower() == next_room["name"].lower():
                self.current_room = next_room
                self.map.set_current_room(self.current_room)
                self.map.increment_room_count()
                print(f"You move to the {self.current_room['name']}.")
                return
            # Check if command is a direction
            elif self.map.is_move_valid(destination.lower()):
                # Checks for last condition to prevent moving at the last room
                self.current_room = next_room
                self.map.set_current_room(self.current_room)
                self.map.increment_room_count()
                print(f"You move to the {self.current_room['name']}")
                return
            else:
                print(
                    "You can't go that way. Try another way: north, south, east, or west.")

        return
    
    def move_back(self):
        if self.room_history:
            # Pop the last room from the history
            self.current_room = self.room_history.pop()
            self.map.set_current_room(self.current_room) 
            self.map.room_count -= 1
            print(f"You moved back to {self.current_room['name']}.")
        else:
            print("You can't move back any further.")



    def get_interactive_items_descriptions(self):
        descriptions = []
        for item_name in self.current_room["interactive_items"]:
            description = self.objects.get_description(item_name)
            descriptions.append(description)
        return descriptions

    def take_item_from_room(self, item):
        item = item.lower()

        for room_item in self.current_room["interactive_items"]:
            if item == room_item.lower():
                item_location = self.current_room["interactive_items"].pop(
                    room_item)
                return room_item, item_location
        
        return None, None

    def add_item_to_room(self, item, location):
        self.current_room["interactive_items"].update({item: location})
        # self.objects.set_object_presence(item, True)
        print(f"You've added the {item} to the room.")

    def drop_item(self, item):
        inventory_item__value = self.inventory.get_item(item)
        if inventory_item__value:
            self.add_item_to_room(item.lower(), inventory_item__value)
            self.inventory.remove_item(item.lower())
            print(f"You dropped the {item}.")
        else:
            print("You don't have that item in your inventory.")
