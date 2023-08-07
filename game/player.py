from game.inventory import Inventory


class Player:
    def __init__(self, name, starting_room, game_map, objects):
        self.name = name
        self.current_room = starting_room
        self.map = game_map
        self.objects = objects
        self.inventory = Inventory()
        self.room_history = []
        self.visited_rooms = set()
        self.visited_rooms.add(self.current_room["name"])


    def serialize(self):
        return {
            "name": self.name,
            "current_room": self.current_room["name"],
            "inventory": self.inventory.serialize(),
            "visited_rooms": list(self.visited_rooms) 
        }

    @classmethod
    def deserialize(cls, data, map_obj, objects_obj):
        current_room = map_obj.get_room_by_name(data["current_room"])
        player = cls(data["name"], current_room, map_obj, objects_obj)
        player.inventory.deserialize(data["inventory"])
        
        # Add this line to restore the visited rooms from the saved game data
        if "visited_rooms" in data:
            player.visited_rooms = set(data["visited_rooms"])
        
        return player

    def get_name(self):
        return self.name
    
    def move(self, destination):
        next_room = self.map.get_next_room()
        self.room_history.append(self.current_room)

        if next_room:
            if destination.lower() == next_room["name"].lower():
                self.current_room = next_room
            elif self.map.is_move_valid(destination.lower()):
                self.current_room = next_room
            else:
                print("You can't go that way. Try another way: north, south, east, or west.")
                return

            if self.current_room["name"] not in self.visited_rooms:
                print(self.current_room["description"])
                self.visited_rooms.add(self.current_room["name"])
            else:
                print(self.current_room["short_description"])
            self.map.set_current_room(self.current_room)
            self.map.increment_room_count()


    def move_back(self):
        if self.room_history:
            self.current_room = self.room_history.pop()

            if self.current_room["name"] not in self.visited_rooms:
                print(self.current_room["description"])
            else:
                print(self.current_room["short_description"])

            self.map.set_current_room(self.current_room) 
            self.map.room_count -= 1
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
        print(f"You've added the {item} to the room.")

    def drop_item(self, item):
        inventory_item__value = self.inventory.get_item(item)
        if inventory_item__value:
            self.add_item_to_room(item.lower(), inventory_item__value)
            self.inventory.remove_item(item.lower())
            print(f"You dropped the {item}.")
        else:
            print("You don't have that item in your inventory.")
