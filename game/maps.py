import json


class Map:
    def __init__(self):
        with open("data/maps.json", 'r') as file:
            data = json.load(file)

        self.map_data = data["maps"]
        self.room_count = 1
        self.current_room = self.map_data[list(self.map_data.keys())[0]]

    def serialize(self):
        return {
            "room_count": self.room_count,
            "current_room": self.current_room,
        }

    def deserialize(self, data):
        self.room_count = data["room_count"]
        self.current_room = data["current_room"]

    def get_current_room(self):
        return self.current_room
    
    def get_room_by_name(self, room_name):  
        """
        Returns the room data based on the given room name.
        """
        for room_key in self.map_data:
            if self.map_data[room_key]["name"].lower() == room_name.lower():
                return self.map_data[room_key]
        return None

    def is_move_valid(self, direction):
        """checks the current room valid moves"""
        try:
            valid_moves = self.current_room['valid_moves']
            # Checks if the direction is in the valid moves dictionary and check if it is true
            if direction in valid_moves and valid_moves[direction]:
                return True
            else:
                return False
        except KeyError:
            print("Wrong direction input")
            return False

    def set_current_room(self, room):
        """Sets the current room"""
        self.current_room = room

    def get_next_room(self):
        """moves linear to next room if right direction chosen"""
        room_keys = list(self.map_data.keys())
        if self.room_count > len(room_keys) - 1:
            print(
                "You are already at the last room. Cannot go further. Pull the victory bell for a message!")
            return False

        return self.map_data[room_keys[self.room_count]]

    def get_room_names(self):
        """Returns a list of room names"""
        return [self.map_data[room_key]["name"].lower() for room_key in self.map_data]

    def increment_room_count(self):
        """Increments the room count"""
        self.room_count += 1

    def get_interactive_items_descriptions(self):
        descriptions = []
        for item_name in self.current_room["interactive_items"]:
            description = self.objects.get_description(item_name)
            descriptions.append(description)
        return descriptions




